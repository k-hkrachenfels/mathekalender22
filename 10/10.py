
import numpy as np
import torch

#weihnachtsmann möchte Arne, Coco, Dante, Enzo und Henri 
p = [ 1, 0, 1, 1, 1, 0, 0, 1, 0, 0]
success = torch.tensor([ True, False, True, True, True, False, False, True, False, False])

# matrix where each colum corresponds to the preferrence and doubling 
# the lements in the diagonally
preferred = torch.tensor([p*10]).view(10,10)+torch.eye(10) 

for i in range(10):
    for j in range(i,10):
        for k in range(j,10):
            mat = torch.tensor(
            # voting yourself is scored as 2
           [[ 2, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [ 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [ 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [ 0, 0, 0, 0, 2, 1, 0, 1, 0, 1],
            [ 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [ 0, 0, 1, 0, 1, 0, 2, 1, 0, 0],
            [ 0, 0, 0, 1, 0, 0, 1, 2, 0, 1],
            [ 0, 0, 1, 0, 0, 0, 0, 0, 2, 1],
            [ 0, 1, 0, 0, 1, 0, 0, 1, 1, 0]])
            mat[i] = preferred[i]
            mat[j] = preferred[j]
            mat[k] = preferred[k]
            vote = mat.sum(dim=0)
            proposal = vote>=5
            if proposal.allclose(success):
                print("done", i, ", ",j,", ",k)
