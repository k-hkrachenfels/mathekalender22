import numpy as np


cost_matrix = np.array([
            [2, 4, 1000000, 1000000 , 5, 8],
            [7, 8, 8, 11, 3, 5],
            [8, 6, 5, 4 , 9, 9]])
            
shipments=np.array([
 [ 100, 325 ,  0 ,  0 , 75 ,  0],
 [  0,   0 ,  0 ,  0 ,125 ,275],
 [  0, 125 ,300 ,400 ,  0 , 75]])

print(sum(sum(cost_matrix*shipments)))