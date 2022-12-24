
from util.constant_set import ConstantSet
import itertools
import math
import numpy as np
from tqdm import tqdm


class SHAPE(ConstantSet):
    SQUARE = 2
    CIRCLE = 1
    RHOMB = 0

shape_dict = {
    SHAPE.CIRCLE: "circle",
    SHAPE.RHOMB:  "rhomb ",
    SHAPE.SQUARE: "square "
}

def check_order(a,i,j):
    shape1=a[i,j-1,1]
    shape2=a[i,j,1]

    if not shape1>=shape2:
        return False
    return True
    
def check_ver(a,i,j):
    
    num1=a[i-1,j,0]
    num2=a[i,j,0]
    shape1=a[i-1,j,1]
    shape2=a[i,j,1]

    if shape1==SHAPE.SQUARE and shape2==SHAPE.SQUARE:
        if not num1 > num2:
            return False
    
    if shape1==SHAPE.CIRCLE and shape2==SHAPE.SQUARE:
        if not num1 >= num2:
            return False

    if shape1==SHAPE.RHOMB and shape2 == SHAPE.SQUARE:
        if not num1 >= num2:
            return False



    if shape1==SHAPE.SQUARE and shape2==SHAPE.CIRCLE:
        if not num1 > num2:
            return False
    
    if shape1==SHAPE.CIRCLE and shape2==SHAPE.CIRCLE:
        if not num1 > num2:
            return False

    if shape1==SHAPE.RHOMB and shape2 == SHAPE.CIRCLE:
        if not num1 > num2:
            return False


   
    if shape1==SHAPE.SQUARE and shape2==SHAPE.RHOMB:
        if not num1 > num2:
            return False
    
    if shape1==SHAPE.CIRCLE and shape2==SHAPE.RHOMB:
        if not num1 >= num2:
            return False

    if shape1==SHAPE.RHOMB and shape2 == SHAPE.RHOMB:
        if not num1 > num2:
            return False
    return True
         
def check_hor(a,i,j):
    num2=a[i,j,0]
    shape2=a[i,j,1]
    j=j-1
    while j>=0:
        num1=a[i,j,0]
        shape1=a[i,j,1]
        if shape1==SHAPE.SQUARE and shape2==SHAPE.SQUARE:
            if not num1 < num2:
                return False
        if shape1==SHAPE.CIRCLE and shape2==SHAPE.CIRCLE:
            if not num1 > num2:
                return False
        if shape1==SHAPE.RHOMB and shape2==SHAPE.RHOMB:
            if not num1 < num2:
                return False
        j=j-1
    return True


def choose(a, i, j, parts):
    for part in parts:
        a[i,j]=part
        if i>0:
            if not check_ver(a,i,j):
                continue
            if not check_order(a,i,j):
                continue

        if j>0:
            if not check_hor(a,i,j):
                continue
            

        cparts = parts.copy()
        cparts.remove(part)
       
        ca = a.copy()
        if j<2:
            yield from choose(ca, i, j+1, cparts)
        
        if i<3:
            yield from choose(ca, i+1, 0, cparts)

        if i==3 and j==2:
            yield(ca)
    

values = [(i,j) for i in range(4) for j in SHAPE.values]
a = np.zeros((4,3,2),dtype=int)
for c,a in enumerate(choose(a,0,0,values)):
    for i in range(4):
        for j in range(3):
            shape=a[i,j,1]
            num=a[i,j,0]
            print(f"{shape_dict[shape]},{num} ",end="")
        print()
    print()
    print(c)
    break

#print(math.factorial(3)*math.factorial(4))


 
  

    
    




