# todo: map class can track and save the routes as .csv or something else
import numpy as np
# import node


class Map:
    def __init__(self, node_list: dict, paths: np.ndarray, pheromones: np.ndarray):
        self.N = 1000
        self.node_list = node_list # {1: x,y, , 2, 3, etc.}
        self.paths = paths # [[1, 2], [3, 2], etc.] [index, index, pheromone] always smaller index at the front
        self.pheromone = pheromones # [100]
        self.graph = [[] for i in range(self.N)]
        self.cycles = [[] for i in range(self.N)]

    def add_connection(self, connection: np.ndarray):
        np.append(self.paths, connection, axis=0)

    def compute_length(self, index1: int, index2: int):
        return np.sum(np.square(self.node_list[index1]['position'] - self.node_list[index2]['position']))

    def update_array_length(self): # if the array are to short to track the connections
        pass

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

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Function to print the cycles
    def printCycles(self, edges, mark: list):

        # push the edges that into the
        # cycle adjacency list
        for i in range(1, edges + 1):
            if mark[i] != 0:
                self.cycles[mark[i]].append(i)

        # print all the vertex with same cycle
        for i in range(1, cyclenumber + 1):

            # Print the i-th cycle
            print("Cycle Number %d:" % i, end=" ")
            for x in self.cycles[i]:
                print(x, end=" ")
            print()

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