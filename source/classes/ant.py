# todo ant class reacts to pheromone and create pheromone

"""
this file contains at least two classes
ant class

"""
import numpy as np

class Ant:
    def __init__(self, position: int, nodes: list):
        """position = index of current node, nodes = must visit nodes, path = travelled path, visited = already visited nodes (must visit nodes)
        visited_all : a bolean to check if a ant has visited all must visit nodes"""
        self.nodes = nodes
        self.path = []
        self.position = position
        self.visited = [position]
        self.visited_all = False
    
    def update_position(self, newPos: int):
        """updates the position of the ant"""
        #get the travelled edge
        travelled_edge = (self.position, newPos)
        travelled_edge = (min(travelled_edge), max(travelled_edge))
        
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
        self.path.append(edge)
        


def move_ant(ant: Ant):
    """moves an Ant to a new node"""
    """rewrite to ask map an index -> map returns the possible next ones and their prob"""
    # possible = nodes.connect(ant.position) #i somehow need the possible conections from a given node
    
    # smart_choice_prob = 0.75 #probability to make the optimal choice
    # #make not smart choice
    # if(not (rd.random() < smart_choice_prob)):
    #     ant.update_position(np.choice(possible, 1))
    
    # #find the best next choice -> assumption pheromones are saved as a tuple (i,j)
    # best_next = (possible[0], pheromones[ant.pos, possible[0]])
    # for i in range(1, len(possible)):
    #     pheromones_onedge = pheromones[ant.pos, possible[i]]
    #     if  pheromones_onedge > best_next[1]:
    #         best_next = (possible[i], pheromones_onedge)
            
    # ant.update_position(best_next[0])
    
    possible = Map.get_possible(ant.pos)
    
    move_to = np.random.choice(index, p = prob)#index index list, prob = probabilities
    
    ant.update(move_to)
    pass
    
    
    
            