from pulp import makeDict, lpSum, LpProblem, LpMinimize, LpVariable, LpInteger, LpStatus


import random
import numpy as np
import scipy.optimize

N_CONSUMERS = 6
N_FACTORIES = 3

supplies = {"A": 500, "B": 400, "C": 900}

# Creates a list of all demand nodes
consumers = ["1", "2", "3", "4", "5", "6"]

# Creates a dictionary for the number of units of demand for each demand node
demands = {
    "1": 100,
    "2": 450,
    "3": 300,
    "4": 400,
    "5": 200,
    "6": 350,
}

hour_costs = [  
    [2, 4, 1000000, 1000000, 5, 8], # A
    [7, 8,       8,      11, 3, 5], # B    
    [8, 6,       5,      4 , 9, 9]  # C
]

cost = np.random.rand(N_CONSUMERS, N_FACTORIES) # c
demand = np.random.rand(N_CONSUMERS) # b_eq
capacity = [250, 300, 500, 750, 100, 200] # b_ub

A_eq = np.zeros(N_CONSUMERS*N_FACTORIES*N_CONSUMERS).reshape(N_CONSUMERS, N_CONSUMERS*N_FACTORIES)
# Constraint for each lane, sum over the available carriers
for l in range(N_CONSUMERS):
    for var in range(l*N_FACTORIES, l*N_FACTORIES+N_FACTORIES):
        A_eq[l, var] = 1

A_ub = np.zeros(N_FACTORIES*N_CONSUMERS*N_FACTORIES).reshape(N_FACTORIES, N_CONSUMERS*N_FACTORIES)
# Constraint for each carrier, sum over the lanes
for c in range(N_FACTORIES):
    for var in range(c, N_CONSUMERS*N_FACTORIES, N_FACTORIES):
        A_ub[c, var] = 1

print(scipy.optimize.linprog(cost.flatten(), A_eq=A_eq, b_eq=demand, 
    A_ub=A_ub, b_ub=capacity, options={"maxiter": 10000}))



# Creates a list of all the supply nodes
factories = ["A", "B", "C"]

# Creates a dictionary for the number of units of supply for each supply node


# The cost data is put into a dictionary
costs = makeDict([factories, consumers], hour_costs, 0)

# Creates the 'prob' variable to contain the problem data
prob = LpProblem("Beer Distribution Problem", LpMinimize)

# Creates a list of tuples containing all the possible routes for transport
routes = [(f, c) for c in consumers for f in factories]

# A dictionary called 'Vars' is created to contain the referenced variables(the routes)
vars = LpVariable.dicts("Route", (factories, consumers), 0, None, LpInteger)

# The objective function is added to 'prob' first
prob += (
    lpSum([vars[f][c] * costs[f][c] for (f, c) in routes]),
    "Sum_of_Transporting_Costs",
)

# The supply maximum constraints are added to prob for each supply node (warehouse)
for f in factories:
    prob += (
        lpSum([vars[f][c] for c in consumers]) == supplies[f],
        f"Sum_of_Products_out_of_Warehouse_{f}",
    )

# The demand minimum constraints are added to prob for each demand node (bar)
for c in consumers:
    prob += (
        lpSum([vars[f][c] for f in factories]) == demands[c],
        f"Sum_of_Products_into_Bar{c}",
    )

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

