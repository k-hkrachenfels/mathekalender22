
import random, math
import torch
import grid
from net.net import DQN, MLP
from util.replay import ReplayMemory
from grid import Field, Direction
import torch
from torch import nn
import torch.optim as optim
from collections import namedtuple
from grid import Env
from itertools import count
from grid import Visualize


BATCH_SIZE = 128
GAMMA = 0.999
EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 20000
TARGET_UPDATE = 500
H=5
W=5
REPL_MEM_SIZE=1000

Transition = namedtuple('Transition', ('state', 'action', 'next_state', 'reward'))
        
class Model(object):
    def __init__(self, num_actions, num_channels):
        
        # if gpu is to be used
        self.num_actions = num_actions
        self.device = torch.device("mps" if torch.cuda.is_available() else "cpu")
        self.policy_net = MLP(H, W, num_channels, self.num_actions, self.device).to(self.device)
        self.target_net = MLP(H, W, num_channels, self.num_actions, self.device).to(self.device)
        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.target_net.eval()
        self.optimizer = optim.RMSprop(self.policy_net.parameters(),
        lr = 1e-3,
        momentum = 0.01,
        alpha = 0.99,
        eps = 1e-8,
        centered =True,
        weight_decay =0)
        self.memory = ReplayMemory(REPL_MEM_SIZE, Transition)
        self.steps_done = 0

    def select_action(self, state: Env):
        sample = random.random()
        eps_threshold = EPS_END + (EPS_START - EPS_END) * \
            math.exp(-1. * self.steps_done / EPS_DECAY)
        self.steps_done += 1
        if sample > eps_threshold:
            print(".",end="")
            with torch.no_grad():
                # t.max(1) will return largest column value of each row.
                # second column on max result is index of where max element was
                # found, so we pick action with the larger expected reward.
                policy_net_action = self.policy_net(state).max(1)[1].view(1, 1)
                #if policy_net_action in state.get_possible_actions():
                return policy_net_action
        else:
            print("x",end="")
        
        actions = state.get_possible_actions()
        action_samples = random.sample(actions,1)
        action_ordinal = Direction.ordinal(action_samples[0])
        return torch.tensor([[action_ordinal]], device=self.device, dtype=torch.long)

    def optimize_model(self):
        if len(self.memory) < BATCH_SIZE:
            return
        transitions = self.memory.sample(BATCH_SIZE)
        # Transpose the batch (see https://stackoverflow.com/a/19343/3343043 for
        # detailed explanation). This converts batch-array of Transitions
        # to Transition of batch-arrays.
        batch = Transition(*zip(*transitions))

        # Compute a mask of non-final states and concatenate the batch elements
        # (a final state would've been the one after which simulation ended)
        non_final_mask = torch.tensor(tuple(map(lambda s: s is not None,
                                            batch.next_state)), device=self.device, dtype=torch.bool)
        non_final_next_states = torch.cat([s for s in batch.next_state
                                                    if s is not None])
        state_batch = torch.cat(batch.state)
        action_batch = torch.cat(batch.action)
        reward_batch = torch.cat(batch.reward)

        # Compute Q(s_t, a) - the model computes Q(s_t), then we select the
        # columns of actions taken. These are the actions which would've been taken
        # for each batch state according to policy_net
        state_action_values = self.policy_net(state_batch).gather(1, action_batch)

        # Compute V(s_{t+1}) for all next states.
        # Expected values of actions for non_final_next_states are computed based
        # on the "older" target_net; selecting their best reward with max(1)[0].
        # This is merged based on the mask, such that we'll have either the expected
        # state value or 0 in case the state was final.
        next_state_values = torch.zeros(BATCH_SIZE, device=self.device)
        next_state_values[non_final_mask] = self.target_net(non_final_next_states).max(1)[0].detach()
        # Compute the expected Q values
        expected_state_action_values = (next_state_values * GAMMA) + reward_batch

        # Compute Huber loss
        criterion = nn.SmoothL1Loss()
        loss = criterion(state_action_values, expected_state_action_values.unsqueeze(1))

        # Optimize the model
        self.optimizer.zero_grad()
        loss.backward()
        for param in self.policy_net.parameters():
            param.grad.data.clamp_(-1, 1)
        self.optimizer.step()

    def train(self, state: Env):
        i=0
        num_episodes = 50
        acc_reward=0
        done=False
        for i_episode in range(num_episodes):
            for t in count():
                i+=1
                # Select and perform an action
                #if state.is_final():
                if done or state is None:
                    state = grid.EnvBuilder.build(W,H)
                    done=False
                    print("")

                assert state is not None
                action = self.select_action(state)
                # if action in state.get_possible_actions():
                #     reward = torch.tensor([reward], device=self.device)
                # else:
                #     reward = -10
                transition = state.step(action)

                reward = transition.reward
                next_state = transition.next_state
                reward = torch.tensor([reward], device=self.device)
                acc_reward+=reward
                #done = len(next_state.get_possible_actions())==0
                state_field = state.to(self.device) 
                next_state_field = next_state.to(self.device) if next_state is not None else state.to(self.device)

                # Store the transition in memory
                self.memory.push(state_field, action, next_state_field, reward)

                # Move to the next state
                state = next_state
                #Visualize.visualize(state)

                # Perform one step of the optimization (on the policy network)
                self.optimize_model()
                if reward==0 or state.is_final():
                    if reward==0:
                        print("-inv!",end="")
                    done=True
                    #if state:
                    #    Visualize.visualize(state,i)
                    print(f"done, reward={acc_reward}")
                    acc_reward=0

                # Update the target network, copying all weights and biases in DQN
                if t % TARGET_UPDATE == 0:
                    #Visualize.visualize(state)
                    self.target_net.load_state_dict(self.policy_net.state_dict())
                    self.test()

    def test(self):
        finished=False
        state = grid.EnvBuilder.build(W,H)
        while not finished:
            Visualize.visualize(state)
            action = self.target_net(state).max(1)[1].view(1, 1)
            print(f"action={Direction.value(action)}")
            transition = state.step(action)
            next_state = transition.next_state
            if next_state==None or next_state.is_final():
                Visualize.visualize(state)
                finished=True
            else:
                state=next_state

       

