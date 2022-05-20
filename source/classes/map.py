# todo: map class can track and save the routes as .csv or something else
import numpy as np
import node


class Map:
    def __init__(self, node_list: dict, paths: np.ndarray, pheromones: np.ndarray):
        self.node_list = node_list # {1: x,y, , 2, 3, etc.}
        self.paths = paths # [[1, 2, 100], [3, 2, 42], etc.] [index, index, pheromone] always smaller index at the front
        self.pheromone = pheromones

    def add_connection(self, connection: np.ndarray):
        np.append(self.paths, connection, axis=0)

    def compute_length(self, index1: int, index2: int):
        return np.sum(np.square(self.node_list[index1]['position'] - self.node_list[index2]['position']))

    def update_array_length(self): # if the array are to short to track the connections
        pass

    def create_node(self, index, position, real):
        self.node_list[index] = {"position": position, "real": real}


    def dfs(self):
        pass

    def evaporate(self, evaporation=0.9): # how to update new connections with low costs
        for path in self.paths:
            path[2] *= evaporation

    def add_new_pheromones(self, ants_path: list):
        for ant in ants_path:
            for path in ant:
                if path[0] < path[1]:
                    index = np.where([path[0], path[1]])
                else:
                    index = np.where([path[1], path[0]])
                self.pheromone[index] += 1

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