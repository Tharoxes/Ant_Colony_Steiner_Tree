# todo ant class reacts to pheromone and create pheromone

"""
this file contains at least two classes
ant class

"""

class Ant:
    def __init__(self, position):
        """position = index of current node, nodes = must visit nodes, path = travelled path, visited = already visited nodes (must visit nodes)
        visited_all : a bolean to check if a ant has visited all must visit nodes"""
        self.nodes = []
        self.path = []
        self.position = position
        self.visited = []
        self.visited_all = False
    
    def update_position(self, pos):
        self.position = pos
        if(pos in self.nodes and not pos in self.visited):
            self.visited.append(pos)
            
        if len(self.visited) == len(self.nodes):
            self.visited_all = True
        
        
    def update_path(self, edge: tuple):
        if(edge in self.path): return
        if((edge[1], edge[0]) in self.path): return 
        
        self.path.append(edge)
        

        
    
        
        