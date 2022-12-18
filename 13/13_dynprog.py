from typing import Tuple
from util.constant_set import ConstantSet
import numpy as np
from PIL import Image
from collections import namedtuple
from copy import deepcopy, copy
from abc import abstractmethod, ABC
from functools import cache



class Field(ConstantSet):
    A = 1 
    SCHOKOLADE = 0 
    GELEE = 3 

class Player(ConstantSet):
    ALTO = True
    BILBO = False

field_images = {
    Field.A: '13/tiles/a.png',
    Field.SCHOKOLADE: '13/tiles/empty.png',
    Field.GELEE :'13/tiles/gelee.png'
}


N=5

def increment(a, column, max_row):
    if column>=len(a):
        return False
    new_max_row = min(a[column],max_row)
    # try to find a column to the right with less than max_row fields set
    if increment(a, column+1, new_max_row):
        return True
    else:
        # all columns to the right already have the same size
        # we try if we can increase the current column
        if a[column]<max_row:
            # we can
            a[column]+=1
            return True
        else:
            # we are already filled 
            # no more moves possible
            return False

def move( state, x, y):
    for col in range(x):
        if state[col]<y:
            state[col]=y
    return state


class WinTree:
    """a tree that keeps track of all win states with a fast lookup scheme"""
    def __init__(self, num_columns) -> None:
        self.num_columns = num_columns
        self.root = [None]*num_columns
    
    def add_state(self,a):
        if(len(a)==0):
            return
        current = a[0]
        if self.root[current]==None:
            self.root[current]=WinTree(self.num_columns)
        self.root[current].add_state(a[1:])

    def is_win(self,a):
        # check if a is element in tree
        if len(a)==0:
            return True
        child = self.root[a[0]]
        if child:
            return child.is_win(a[1:])
        else:
            return False


    def __repr__(self):
        result=[]
        for i, subtree in enumerate(self.root):
            if subtree:
                for sublist in subtree.__repr__():
                    tail = [i]
                    tail.extend(sublist)
                    result.append(tail)
        if len(result)==0:
            return [[]]
        else:
            return result
           
    def __str__(self):
        return str(self.__repr__())

def visualize(s, rows, columns, tag=""):
    TILE_SIZE_X = 172
    TILE_SIZE_Y = 174
    
    state = np.zeros((rows,columns),dtype=int)
    for column,row in enumerate(s):
        state[column,:row]=Field.A
    img = Image.new(mode='RGB', size=(TILE_SIZE_X*N, TILE_SIZE_Y*N))
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
    
def test():
    # initialize new Board with COL columns
    ROWS=3
    COLS=3
    a = [0]*COLS

    # get all possible states when board has ROWS rows

    while increment(a,0,ROWS):
        print(a)

    visualize([3,2,1],rows=ROWS,columns=COLS)

    # manually construct simple tree
    tree1 = WinTree(ROWS+1)
    tree2 = WinTree(ROWS+1)
    tree3 = WinTree(ROWS+1)
    tree4 = WinTree(ROWS+1)
    tree3.root[2]=tree4
    tree2.root[2]=tree3
    tree1.root[3]=tree2
    print(tree1)        
    print(f"tree1.is_win([3,2,2] = {tree1.is_win([3,2,2])}")   
    print(f"tree1.is_win([3,2,1] = {tree1.is_win([3,2,1])}")   

    tree = WinTree(num_columns=4) 
    tree.add_state([1,1,1])
    print(f"tree.is_win([3,2,2] = {tree.is_win([3,2,2])}")   
    print(f"tree.is_win([3,2,1] = {tree.is_win([3,2,1])}")   
    state=[1,1,1]
    visualize(state,rows=ROWS,columns=COLS)  
    state=move(state,2,2)  

    visualize(state,rows=ROWS,columns=COLS,tag="m")  

@cache
def final_state_str(ROWS):
    final_state_str = str([ROWS]*ROWS)
    return final_state_str

def is_win( tree, s, ROWS):
    print(s)
    if str(s) == final_state_str(ROWS):
        return False

    while increment(s,0,ROWS):
        state=s.copy()
        # try lookup
        if tree.is_win(state):
            return True, None
        win_opponent = is_win(tree, state, ROWS)
        if not win_opponent:
            # update lookup
            tree.add_state(state)
            return True, None    
        
    return False,s

if __name__ == "__main__":  
    # initialize new Board with COL columns
    ROWS=3
    COLS=3
    a = [0]*COLS
    win_tree = WinTree(ROWS+1)
    #win_tree.add_state([3,3,3])

    w,state=is_win(win_tree,[1,0,0],ROWS)
    print(w,state)




   



    # COLS=3
    # ROWS=3
    # s = State()
    # state = np.array((COLS),dtype=int)
    # visualize(s, ROWS, COLS)
    # # print(s.find_children(state))
    # # print(s.shape)

    # # board = Board(7,4)
    # x = int(input("x="))
    # y = int(input("y="))
    # s = move(s,x,y)

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



