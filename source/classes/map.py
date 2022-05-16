# todo: map class can track and save the routes as .csv or something else
import numpy as np
import node


class Map:
    def __init__(self, node_list: dict, paths: np.ndarray):
        self.node_list = node_list # {1: x,y, , 2, 3, etc.}
        self.paths = paths # [[1, 2, 100], [3, 2, 42], etc.] [index, index, pheromone] always smaller index at the front

    def add_connection(self, connection: np.ndarray):
        np.append(self.paths, connection, axis=0)

    def compute_length(self, index1: int, index2: int):
        return np.sum(np.square(self.node_list[index1].pos - self.node_list[index2].pos))

    def update_array_length(self): # if the array are to short to track the connections
        pass

    def create_node(self, index, position, real):
        new_Node = node.Node(index, position, real)
        np.append(self.node_list, new_Node)

    def dfs(self):
        pass

    def update_pheromones(self): # how to update new connections with low costs
        pass

    def get_possible_paths(self, ant_pos: int):
        possible_paths = []
        for path in self.paths:
            if ant_pos == path[0]:
                possible_paths.append(path[1:3])
            elif ant_pos == path[1]:
                possible_paths.append(path[0, 2])
        possible_paths = np.asarray(possible_paths)
        sum = np.sum(possible_paths, axis=0)
        sum = sum[1]
        possible_paths = possible_paths[:,-1] / sum
        return possible_paths