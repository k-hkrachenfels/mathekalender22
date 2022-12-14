from typing import Tuple
from attrs import define, field
from util.constant_set import ConstantSet
import numpy as np
from PIL import Image
import torch
import inspect
from collections import namedtuple
from copy import deepcopy, copy
from mcts import Node
from functools import cache
import random
import xxhash


class Field(ConstantSet):
    A = 1 
    B = 2 
    EMPTY = 0 
    GELEE = 3 

class Player(ConstantSet):
    ALTO = True
    BILBO = False


field_images = {
    Field.A: '13/tiles/a.png',
    Field.B: '13/tiles/b.png',
    Field.EMPTY: '13/tiles/empty.png',
    Field.GELEE :'13/tiles/gelee.png'
}

#@define
class Board(Node):
    def __init__(self,xmax,ymax,):
        self.xmax = xmax
        self.ymax = ymax
        self.state = np.zeros((xmax,ymax))
        self.state[xmax-1,ymax-1]=Field.GELEE
        x=2
        y=0
        self.state[:x+1,:y+1]=Field.A
        x=1
        y=1
        self.state[:x+1,:y+1]=Field.B


    def visualize(self, state, i):
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
        img.save(f'13/output/out{i}.png')
        print("Board visualized")


    #@cache
    def find_children(self, state):
        children = np.transpose((state==Field.EMPTY).nonzero())
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

    def draw(self, state, move):
        x,y = move
        state[:x+1,:y+1]=Field.A

    def altoDraw(self, state, num_moves: int) -> bool:
        for move in self.find_children(state):
            next_state = state.copy()
            self.draw(next_state, move)
            win, states = self.bilboDraw(next_state, num_moves+1)
            if win==Player.ALTO:
                print("alto  ", num_moves, "->", move)
                states.append(state)
                return Player.ALTO, states
        return Player.BILBO,[state]

    def find_all_altoDraw(self, state, num_moves: int) -> bool:
        win = Player.BILBO
        for move in self.find_children(state):
            next_state = state.copy()
            self.draw(next_state, move)
            win, states = self.bilboDraw(next_state, num_moves+1)
            if win==Player.ALTO:
                print("alto  ", num_moves, "->", move)
                states.append(state)
                return Player.ALTO, states
        return Player.BILBO,[state]

    def bilboDraw(self, state, num_moves: int) -> bool:
        for move in self.find_children(state):
            next_state = state.copy()
            self.draw(next_state, move)
            win, states = self.altoDraw(next_state, num_moves+1)
            if win==Player.BILBO:
                states.append(state)
                return Player.BILBO, states
        return Player.ALTO,[state]

    #impl abstractmethod
    def __hash__(self):
        "Nodes must be hashable"
        return xxhash.xxh32_intdigest(self.state.data.tobytes())


    #impl abstractmethod
    def __eq__(node1, node2):
        "Nodes must be comparable"
        return node1.__hash__() == node2.__hash__()
        

# def rollout(state):
#     print(state)
#     possible_actions = state.get_possible_actions()
#     while len(possible_actions)>0:
#         action = np.random.choice(possible_actions,1)[0]
#         action_ordinal = Direction.ordinal(action)
#         print(f"action={action}")
#         transition = state.step(action_ordinal)
#         state, action, next_state, reward = transition
#         state = next_state
#         possible_actions = state.get_possible_actions()
#     return state

if __name__ == "__main__":  
    board = Board(5,4)
    board.visualize(board.state,"-")
    #children=board.find_children(board.state)

    win,states=board.altoDraw(board.state, 0)
    for i,state in enumerate(states):
        print(state.shape)
        print(state)
        board.visualize(state,i)


    if win==Player.ALTO:
        print(f"player alto wins after {len(states)}")
    else:
        print(f"player bilbo wins after {len(states)}")



