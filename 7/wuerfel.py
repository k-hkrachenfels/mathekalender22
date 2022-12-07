import torch
import numpy as np

def binary(x, bits):
    mask = 2**torch.arange(bits).to(x.device, x.dtype)
    return x.unsqueeze(-1).bitwise_and(mask).ne(0).byte()


ones = torch.Tensor(np.array([1,1,1]))
min_count = 27
max_count = 0
print(ones)
for code in range(2**27):
    if code % 100000 ==0:
        print(".",end="",flush=True)
    b=binary(torch.tensor(code),27)
    #b=binary(code,27)
    w = b.view((3,3,3))
    faces = [w[:,:,0], w[:,:,2] ,w[0,:,:], w[2,:,:], w[:,0,:], w[:,2,:]]

    conditions_hold=True
    for face in faces:
        #print("face=",face)
        row_count = torch.sum(face,dim=0)  
        #print("row_count=",row_count)
        rc_min = torch.min(row_count)
        rc_max = torch.max(row_count)
        #print(rc_min, rc_max)
        if rc_min!=2 or rc_max!=2:
            conditions_hold = False
            break

        #print("face=",face)
        col_count = torch.sum(face,dim=1)  
        #print("row_count=",row_count)
        cc_min = torch.min(row_count)
        cc_max = torch.max(row_count)
        #print(rc_min, rc_max)
        if cc_min!=2 or cc_max!=2:
            conditions_hold = False
            break

    if conditions_hold:
        count = torch.sum(w).numpy()
        if count < min_count:
            min_count = count
        if count > max_count:
            max_count = count
        print(f"min={min_count}, max={max_count}")



