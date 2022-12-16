from typing import Tuple
from util.constant_set import ConstantSet
import numpy as np
from PIL import Image
from collections import namedtuple
from copy import deepcopy, copy
from abc import abstractmethod, ABC
from functools import cache




# field_images = {
#     Field.A: '13/tiles/a.png',
#     Field.B: '13/tiles/b.png',
#     Field.EMPTY: '13/tiles/empty.png',
#     Field.GELEE :'13/tiles/gelee.png'
# }

class Node(ABC):
    """
    A representation of a single board state.
    MCTS works by constructing a tree of these Nodes.
    Could be e.g. a chess or checkers board state.
    """

    @abstractmethod
    def find_children(self):
        "All possible successors of this board state"
        return set()

    @abstractmethod
    def find_random_child(self):
        "Random successor of this board state (for more efficient simulation)"
        return None

    @abstractmethod
    def is_terminal(self):
        "Returns True if the node has no children"
        return True

    @abstractmethod
    def reward(self):
        "Assumes `self` is terminal node. 1=win, 0=loss, .5=tie, etc"
        return 0

    @abstractmethod
    def __hash__(self):
        "Nodes must be hashable"
        return 123456789

    @abstractmethod
    def __eq__(node1, node2):
        "Nodes must be comparable"
        return True
N=1
class State(Node):

    # def __init__(self, initial_state=np.zeros((N),dtype=int)):
    #     self.state = initial_state

    #@cache
    def find_children(self, state, column=0):
        children=set()
        if column == N:
            return children
        elif np.all(state==N+1):
            return []
        else:
            for i in range(state[0],N+1):
                state = state.copy()
                state[column]=i
                children.extend(self.find_children(state,column+1))                
        return children

    def find_random_child(self):
        return super().find_random_child()

    def reward(self):
        return super().reward()

    def is_terminal(self):
        return super().is_terminal()

    def __eq__(node1, node2):
        return super().__eq__(node2)

    def __hash__(self):
        return super().__hash__()


class Game():
    

    def __init__(self, initial=np.zeros((N))):
        self.state = initial
   
    def visualize(self, state, tag=""):
        TILE_SIZE_X = 172
        TILE_SIZE_Y = 174
        xmax = self.xmax
        ymax = self.ymax
        img = Image.new(mode='RGB', size=(TILE_SIZE_X*xmax, TILE_SIZE_Y*ymax))
        for y in range(ymax):
            pos_y = (ymax-y-1) * TILE_SIZE_Y
            for x in range(xmax):
                pos_x = x * TILE_SIZE_X
                pos=(pos_x,pos_y)
                field = state[x,y]
                field_img = field_images[field]
                tile = Image.open(field_img)
                img.paste(tile,pos)
        img.save(f'13/output/out{tag}.png')
        print("Board visualized")


    #@cache
    def find_children(self, state):
        children = np.transpose((state==Field.EMPTY).nonzero())
        np.flip(children,axis=0)
        return children
        

    #impl abstractmethod
    def find_random_child(self):
        "Random successor of this board state (for more efficient simulation)"
        return random.sample(self.find_children(),1)[0]
        

    #impl abstractmethod
    def is_terminal(self, state):
        "Returns True if the node has no children" 
        return len(self.find_children(state))==0

    #impl abstractmethod
    def reward(self):
       pass

    def draw(self, state, move, field):
        x,y = move
        state[:x+1,:y+1]=field

    def altoDraw(self, state, num_moves: int) -> bool:
        states=[state]
        result=Player.BILBO
        for move in self.find_children(state):
            next_state = state.copy()
            self.draw(next_state, move, Field.A)
            win, win_states = self.bilboDraw(next_state, num_moves+1)
            if win==Player.ALTO:
                result=Player.ALTO
                print("alto  ", num_moves, "->", move)
                states.extend(win_states)
                return Player.ALTO, states
        return result,states


    def bilboDraw(self, state, num_moves: int) -> bool:
        states = [state]
        result = Player.ALTO
        for move in self.find_children(state):
            next_state = state.copy()
            self.draw(next_state, move, Field.B)
            win, win_states = self.altoDraw(next_state, num_moves+1)
            if win==Player.BILBO:
                states.extend(win_states)
                return Player.BILBO, states
        return Player.ALTO,states
        

if __name__ == "__main__":  

    s = State()
    state = np.array((N),dtype=int)
    print(s.find_children(state))
    print(s.shape)

    # board = Board(7,4)

    # # play a game as bilbo
    # print(f"board x=",board.xmax,",y=",board.ymax)
    # board.visualize(board.state) 
    # while True:
    #     x = int(input("x="))
    #     y = int(input("y="))
    #     move=(x,y)
    #     print(move)
    #     board.draw(board.state,move,Field.B)
    #     board.visualize(board.state)
    #     win,states=board.altoDraw(board.state, 0)
    #     if win== Player.ALTO:
    #         print("you will loose")
    #     else:
    #         print("you can win")
    #     board.visualize(states[1])
    #     board.state=states[1]


    # if win==Player.ALTO:
    #     print(f"player alto wins after {len(states)}")
    # else:
    #     print(f"player bilbo wins after {len(states)}")



