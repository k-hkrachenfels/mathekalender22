from typing import Tuple
from util.constant_set import ConstantSet
import numpy as np
from PIL import Image
from collections import namedtuple
from copy import deepcopy, copy

class Field(ConstantSet):
    EMPTY = 0 
    LIGHT = 1 
    PASSIVE_LIGHT = 2
    BACKGROUND = 3


field_images = {
    Field.LIGHT: '13/tiles/a.png',
    Field.PASSIVE_LIGHT: '13/tiles/b.png',
    Field.EMPTY: '13/tiles/empty.png',
    Field.BACKGROUND :'13/tiles/gelee.png'
}


class Board():

    def __init__(self):
        self.state = np.ones((8,8))*Field.LIGHT
        self.state[0,2:]=Field.BACKGROUND
        self.state[1,4:]=Field.BACKGROUND
        self.state[2,6:]=Field.BACKGROUND

        self.state[5,6:]=Field.BACKGROUND
        self.state[6,4:]=Field.BACKGROUND
        self.state[7,2:]=Field.BACKGROUND

        self.state[0,0]=Field.PASSIVE_LIGHT
        self.state[1,1]=Field.PASSIVE_LIGHT
        self.state[2,2]=Field.PASSIVE_LIGHT
        self.state[3,3]=Field.PASSIVE_LIGHT
        self.state[4,4]=Field.PASSIVE_LIGHT
        self.state[5,5]=Field.PASSIVE_LIGHT
        self.state[4,7]=Field.PASSIVE_LIGHT
        self.state[7,0]=Field.PASSIVE_LIGHT

   

    def visualize(self, state, tag=""):
        TILE_SIZE_X = 172
        TILE_SIZE_Y = 174
        xmax = state.shape[0]
        ymax = state.shape[1]
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
        img.save(f'16/output/out{tag}.png')
        print("Board visualized")



def find_possible_moves( state):
    children = np.transpose((state==Field.EMPTY).nonzero())
    np.flip(children,axis=0)
    return children.tolist()

def sample( num:int, sampled: list, elements: list):
    if num == 0:
        return [sampled]
    else:
        result=[]
        for i in range(len(elements)):
            element = elements[i]
            celements=elements.copy()
            celements.remove(element)
            csampled = sampled.copy()
            csampled.append(element)
            result.extend(sample(num-1,csampled, celements))
        return result

def propagate(state, moves: list):
    pass
        
# Note: way too many states to be programmatically solvable
if __name__ == "__main__":  
    board = Board()
    board.visualize(board.state)
    possible_moves = find_possible_moves(board.state)
    print(possible_moves)
    s = sample(5, [], possible_moves)
    print(len(s))



    



