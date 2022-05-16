# todo: map class can track and save the routes as .csv or something else
import numpy as np
import node


class Map:
    def __init__(self, node_list: dict, paths: np.ndarray, distances: np.ndarray, index: int):
        self.node_list = node_list # {1: x,y, , 2, 3, etc.}
        self.paths = paths # [[1, 2, 100], [3, 2, 42], etc.] [index, index, pheromone]
        self.distances = distances
        self.index = index

    def add_connection(self, connection: np.ndarray):
        np.append(self.paths, connection, axis=0)

    def compute_length(self):
        pass

    def update_array_length(self): # if the array are to short to track the connections
        pass

    def create_node(self, index, position, real):
        new_Node = node.Node(index, position, real)
        np.append(self.node_list, )

    def dfs(self):
        pass

    def update_pheromones(self): # how to update new connections with low costs
        pass