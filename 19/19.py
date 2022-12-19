import math
import numpy as np
import torch
from torch import nn

FACTORY = [ 500, 400, 900]
STORES = [100, 450, 300, 400, 200, 350 ]
cost_matrix = torch.FloatTensor([
            [2, 4, 10000, 10000 , 5, 8],
            [7, 8, 8, 11, 3, 5],
            [8, 6, 5, 4 , 9, 9]])

class CostModel(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        shipments = torch.rand((3,6))                 #1./cost_matrix
        self.shipments = torch.nn.parameter.Parameter(shipments)

    def forward(self, x):
        return x*torch.abs(self.shipments), self.shipments


model = CostModel()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
np.set_printoptions(precision=2)

for i in range(10000000):
    optimizer.zero_grad()
    out,shipments=model.forward(cost_matrix)
    # loss is quadratic error 
    # based on shipped items per location
    l_store = 100*torch.sum(((torch.sum(shipments, axis=0)-torch.FloatTensor(STORES))/1.)**2)
    # per factory
    l_fac =100*torch.sum(((torch.sum(shipments, axis=1)-torch.FloatTensor(FACTORY))/1.)**2)
    # square of hours needed
    l_hours = (torch.sum(out)**2)/10000.
    loss = l_fac + l_hours + l_store
    if i %10000==0:
        print(f"hours={torch.sum(out).detach().numpy()}",loss.detach().numpy(),l_hours.detach().numpy(),l_store.detach().numpy(),l_fac.detach().numpy())
        print(shipments.detach().numpy().astype(int))
    loss.backward()
    optimizer.step()
print(torch.sum(out).detach().numpy(), loss.detach().numpy())
















