from typing import Tuple
from util.constant_set import ConstantSet
import numpy as np
from PIL import Image
from collections import namedtuple
from copy import deepcopy, copy
from abc import abstractmethod, ABC
from functools import cache
import math

class HashList(list): 
    def __init__(self, *args): 
        # todo: handle constructor with one iterable argument
        super().__init__(args) 
         
    def __hash__(self): 
        return hash(e for e in self)

class Field(ConstantSet):
    A = 1 
    SCHOKOLADE = 0 
    GELEE = 3 

field_images = {
    Field.A: '13/tiles/a.png',
    Field.SCHOKOLADE: '13/tiles/empty.png',
    Field.GELEE :'13/tiles/gelee.png'
}

def is_valid(state):
    if not state:
        return False
    last=math.inf
    for element in state:
        if element>last:
            return False
        last=element
    return True

# handy if we want to fill caches before playing -> maybe not needed because we do not need all states
def enumerate_states(columns, rows):
    #a = [0]*rows
    if columns>0:
        for state in enumerate_states(columns-1,rows):
            for i in range(rows,-1,-1):
                #new_state=[i]
                #new_state.extend(state)
                new_state=state.copy()
                new_state=HashList(*state)
                new_state.append(i)
                if is_valid(new_state):
                    yield(new_state)
    else:
        yield(HashList())
        
def enumerate_moves(a, max_row):
    """ Notes: 
    - we return the moves (in an order that minimizes the number of moves of the oppenent
    by starting in the right upper corner and then going forward in z-style
    - the return is a hashable list of states. This is needed to make the is_win method
    memoizing states it has already seen with @cache annotationl - and thus making it
    a sort of dynamic programming"""
    column = len(a)
    for column in range(len(a)-1,-1,-1):
        for row in range(max_row,-1,-1):
            if a[column]>=row:
                continue
            a_return = a.copy()
            a_return = HashList(*a_return)
            for idx in range(column,-1,-1):
                if a_return[idx] < row:
                    a_return[idx] = row
            yield(a_return)            

def move( state, x, y):
    for col in range(x+1):
        if state[col]<y:
            state[col]=y
    return state

def visualize(s, rows, columns, tag=""):
    TILE_SIZE_X = 172
    TILE_SIZE_Y = 174
    
    state = np.zeros((rows,columns),dtype=int)
    for column,row in enumerate(s):
        state[column,:row]=Field.A
    img = Image.new(mode='RGB', size=(TILE_SIZE_X*columns, TILE_SIZE_Y*rows))
    for y in range(rows):
        pos_y = (rows-y-1) * TILE_SIZE_Y
        for x in range(columns):
            pos_x = x * TILE_SIZE_X
            pos=(pos_x,pos_y)
            field = state[x,y]
            field_img = field_images[field]
            tile = Image.open(field_img)
            img.paste(tile,pos)
    img.save(f'13/output/out{tag}.png')
    print("Board visualized")
    
@cache
def final_state_str(ROWS):
    final_state_str = str([ROWS]*ROWS)
    return final_state_str

@cache
def is_win(start_state, ROWS, depth=0, print_move=False):
    """sort of symmetric min-max -> both players have the same stra"""
    if str(start_state) == final_state_str(ROWS):
        return True, start_state

    for state in enumerate_moves(start_state, ROWS):
        win_opponent = is_win( state, ROWS, depth+1)[0]
        if not win_opponent:
            if print_move:
                visualize(start_state,ROWS,len(start_state),"0")
                visualize(state,ROWS,len(state),"1")
                print(f"winning with move: {start_state} -> {state}")
            return True, state  
    
    return False, None

def init_caches(COLS,ROWS):
    true_count=0
    false_count=0
    for i,state in enumerate(enumerate_states(COLS,ROWS)):
        w=is_win(state,ROWS)[0]
        if w:
            true_count+=1
        else:
            false_count+=1
        print(state, w, true_count, false_count)
        if i%100==0:
            print(".",end="")

if __name__ == "__main__":  
    # initialize new Board with COL columns
    ROWS=10
    COLS=10
    #init_caches(COLS=COLS,ROWS=ROWS)
    #a = [2]*COLS
    a=[10, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    print(a)
    a = HashList(*a)
    while True:
        win,a =is_win(a,ROWS,print_move=True)
        print(win,a)
        if not a:
            exit(0)
        i = int(input("column number start with 0 on the left:"))
        v = int(input("number of pieces to open in the column:"))
        #a[i]=v
        a=move(a,i,v)
        print(a)
        print("computing next move")
