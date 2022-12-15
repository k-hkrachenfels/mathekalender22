from copy import  copy

import math

percentages = {0:0,1:25,2:15,3:10,4:0,5:50,6:0}
edges = {
    0: [1,4],
    1: [0,2,6],
    2: [1,3],
    3: [2,4],
    4: [3,0,5],
    5: [4,6],
    6: [5,1]
  
}
times = {
    (0,1):10,
    (1,0):10,
    (1,2):12,
    (2,1):12,
    (1,6):7,
    (6,1):7,      
    (2,3):15,
    (3,2):15,       
    (3,4):1,
    (4,3):1,  
    (4,5):11,
    (5,4):11,   
    (5,6):8,
    (6,5):8,
    (0,4):10,
    (4,0):10}



class Game():

    def __init__(self):
        pass

    def find_children(self, node, visited_nodes):
        children = []
        for neighbour in edges[node]:
            if not neighbour in visited_nodes:
                children.append(neighbour)
        return children

    def visit(self, visited_nodes, path, accumulated_times=0, accumulated_count=0):
        if len(visited_nodes)==7:
            #print(f"accumulated_count={accumulated_count},path={path}")
            return accumulated_count, path
        
        min_count=math.inf
        best_path = None
        for node in visited_nodes:
            children = self.find_children(node, visited_nodes)
            for child in children:
                time = times[(node,child)]+accumulated_times
                count = percentages[child]*time+accumulated_count
                cvisited_nodes=visited_nodes.copy()
                cvisited_nodes.add(child)
                cpath=path.copy()
                cpath.append(str(node)+"-"+str(child)+",t:"+str(time)+",c:"+str(count))
                returned_count, returned_path = self.visit(
                   visited_nodes=cvisited_nodes, 
                   path=cpath,  
                   accumulated_times=time,
                   accumulated_count=count)
                if returned_count<min_count:
                    min_count=returned_count
                    best_path=returned_path

        return min_count, best_path
            



if __name__ == "__main__":  
    game = Game()
    start_nodes=set()
    start_nodes.add(0)

    path=[]
    min_count, best_path = game.visit(visited_nodes=start_nodes, path=path)
    print(min_count, best_path)

   