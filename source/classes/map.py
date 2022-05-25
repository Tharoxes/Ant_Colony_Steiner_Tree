# todo: map class can track and save the routes as .csv or something else
import numpy as np
# import node


class Map:
    def __init__(self, node_list: dict, paths: np.ndarray, pheromones: np.ndarray):
        self.N = 300
        self.node_list = node_list # {1: x,y, , 2, 3, etc.}
        self.paths = paths # [[1, 2], [3, 2], etc.] [index, index] always smaller index at the front
        self.pheromone = pheromones # relativ values
        self.connections = list()
        self.graph = [[] for i in range(self.N)]
        self.cycles = [[] for i in range(self.N)]
        self.edges = 0
        self.flag_node = len(self.node_list)

    def add_connection(self, connection: np.ndarray):
        np.append(self.paths, connection, axis=0)
        np.append(self.pheromone, np.asarray[[0.4]], axis=0)

    def compute_length(self, index1: int, index2: int):
        return np.sum(np.square(self.node_list[index1]['position'] - self.node_list[index2]['position']))

    def create_node(self, index, position, real):
        self.node_list[index] = {"position": position, "real": real}

    def dfs_cycles(self, u, p, color: list, mark: list, par: list):
        global cyclenumber

        if color[u] == 2:
            return

        # seen vertex, but was not
        # completely visited -> cycle detected.
        # backtrack based on parents to
        # find the complete cycle.
        if color[u] == 1:
            cyclenumber += 1
            cur = p
            mark[cur] = cyclenumber

            # backtrack the vertex which are
            # in the current cycle thats found
            while cur != u:
                cur = par[cur]
                mark[cur] = cyclenumber

            return

        par[u] = p

        # partially visited.
        color[u] = 1

        # simple dfs on graph
        for v in self.graph[u]:

            # if it has not been visited previously
            if v == par[u]:
                continue
            self.dfs_cycles(v, u, color, mark, par)

        # completely visited.
        color[u] = 2

    def addEdges(self, threshhold=0.1):
        connections = self.paths[self.paths > threshhold]
        self.graph = [[] for i in range(self.N)]
        self.edges = 0
        for connection in connections:
            self.edges += 1
            self.graph[connection[0]].append(connection[1])
            self.graph[connection[1]].append(connection[0])

    # Function to print the cycles
    def safe_Cycles(self, edges, mark: list):

        new_cycles = list()
        for i in range(1, edges):
            if mark[i] != 0:
                new_cycles[mark[i]].append(i)

        for j in new_cycles:
            sorted_cycle = j.sort()
            if sorted_cycle not in self.cycles:
                self.cycles.append(sorted_cycle)

    def evaporate(self, evaporation=0.9): # how to update new connections with low costs
        for path in self.paths:
            path[2] *= evaporation

    def add_new_pheromones(self, ants_path: list):
        for ant in ants_path:
            for path in ant:
                if path[0] < path[1]:
                    index = np.where([path[0], path[1]] == self.node_list)
                else:
                    index = np.where([path[1], path[0]] == self.node_list)
                self.pheromone[index] += 1

    def get_possible_paths(self, ant_pos: int):
        possible_paths = []
        for index, path in enumerate(self.paths):
            if ant_pos == path[0]:
                possible_paths.append([path[1], self.pheromone[index]])
            elif ant_pos == path[1]:
                possible_paths.append([path[0], self.pheromone[index]])
        possible_paths = np.asarray(possible_paths)
        sum = np.sum(possible_paths, axis=0)
        sum = sum[1]
        possible_paths = possible_paths[:,-1] / sum
        return possible_paths