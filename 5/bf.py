
import torch
import igraph as ig
import matplotlib.pyplot as plt

N=8


def build_distributions(num_total, num_red):
    count=0
    for i in range(2**num_total):
        if bin(i).count("1")==num_red:
            count+=1

    x = torch.zeros((num_total,count),dtype=torch.int)
    #print(count)
    
    col=0
    for i in range(2**num_total):
        if bin(i).count("1")==num_red:
            for row in range(num_total):  
                x[row,col]=1 if (i//(2**(row)))%2==1 else 0
            col+=1
    return x

def add_edges(i_start,j_start,steps,num_nodes,edges):
    if steps==0:
        return [edges]
    else:
        result=[]
        for i in range(num_nodes):
            for j in range(i+1,num_nodes):
                if i>i_start or i==i_start and j>j_start:
                    edges_cloned = edges.copy()
                    edges_cloned.append((i,j))
                    result.extend(add_edges(i,j,steps-1,num_nodes,edges_cloned))
        return result

def build_adjacency_matrices(num_total,trials):
    input_path=[]
    paths=add_edges(0,0,trials,num_total,input_path)
    adj_matrices = []
    for path in paths:
        A = torch.zeros((8,8),dtype=torch.int)
        for i,j in path:
            A[i,j]=1
            A[j,i]=1
        adj_matrices.append(A)
    return adj_matrices
    
 

def find_solution_for(n, distribs):
    mats=build_adjacency_matrices(8,n)
    print("matrices built")
    for a in mats: 
        r = a.matmul(d)
        lights_on = r.mul(d)
        lights_per_mapping= torch.sum(lights_on,dim=0)
        lowest_num_lights_of_worst_mapping = torch.min(lights_per_mapping)
        if(lowest_num_lights_of_worst_mapping.numpy()!=0):
            print(f"the following matrix defines a strategy for {n}: \n{a}")
            return a
    print(f"There is no solution for {n}")

def visualize(a):
    nodes = []
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if a[i,j] == 1:
                if j>i:
                    nodes.append((i,j))
    g = ig.Graph(N, nodes, directed=False)
    fig, ax = plt.subplots()
    ig.plot(g,
        target=ax,
        layout="circle",
        vertex_label=range(g.vcount()),
        vertex_color="lightblue")
    plt.show()


#d=build_distributions(8,4)
#find_solution_for(6,d) 
#a=find_solution_for(7,d)
a = torch.tensor([[0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0]], dtype=torch.int32)
visualize(a)