
import numpy as np

pos = 0
for step in range(17,0,-1):
    print(f"{pos} -{step}-> ",end="")
    pos+=step
print(pos)