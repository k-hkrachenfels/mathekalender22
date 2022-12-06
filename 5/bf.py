
import torch

N=8


def build_distributions(num_total, num_red):
    count=0
    for i in range(2**num_total):
        if bin(i).count("1")==num_red:
            count+=1

    x = torch.zeros((num_total,count),dtype=torch.int)
    print(count)
    
    col=0
    for i in range(2**num_total):
        if bin(i).count("1")==num_red:
            for row in range(num_total):  
                x[row,col]=1 if (i//(2**(row)))%2==1 else 0
            col+=1
    return x

def add_edges(i_start,j_start,steps,num_nodes,edges):
    if steps==0:
        print(edges)
        return [edges]
    else:
        result=[]
        for i in range(num_nodes):
            for j in range(i+1,num_nodes):
                if i>i or i==i_start and j>j_start:
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
        column_sums= torch.sum(lights_on,dim=0)
        min_column = torch.min(column_sums)
        if(min_column.numpy()!=0):
            print(f"the following matrix defines a strategy for {n}: \n{a}")
            return
    print(f"There is no sulution for {n}")

d=build_distributions(8,4)
#find_solution_for(6,d) 
find_solution_for(7,d)