# todo ant class reacts to pheromone and create pheromone

"""
this file contains at least two classes
ant class

"""

class Ant:
    def __init__(self, position: int):
        """position = index of current node, nodes = must visit nodes, path = travelled path, visited = already visited nodes (must visit nodes)
        visited_all : a bolean to check if a ant has visited all must visit nodes"""
        self.nodes = []
        self.path = []
        self.position = position
        self.visited = [position]
        self.visited_all = False
    
    def update_position(self, newPos: int):
        """updates the position of the ant"""
        #get the travelled edge
        travelled_edge = (self.position, newPos)
        
        #check if the newPos is in the must visit nodes and not already visited
        if(newPos in self.nodes and not newPos in self.visited):
            self.visited.append(newPos)
        
        #checks if all must visit nodes were visited
        if len(self.visited) == len(self.nodes):
            self.visited_all = True
         
        #updates the Ant
        self.update_path(travelled_edge)
        self.position = newPos
        
        
        
    def update_path(self, edge: tuple):
        """helper function for updating a travelled edge"""
        if(edge in self.path): return
        if((edge[1], edge[0]) in self.path): return 
        
        self.path.append(edge)