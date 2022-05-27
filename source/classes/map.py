# todo: map class can track and save the routes as .csv or something else
import numpy as np
# import node


class Map:
    def __init__(self, node_list: dict, paths: np.ndarray, pheromones: np.ndarray):
        self.N = 300
        self.node_list = node_list # {1: x,y, , 2, 3, etc.} dict with np.ndarray and bool
        self.paths = paths # [[1, 2], [3, 2], etc.] [index, index] always smaller index at the front
        self.pheromone = pheromones # relativ values
        self.probability = []
        self.connections = list()
        self.lengths = np.asarray([])
        self.graph = [[] for i in range(self.N)]
        self.cycles = [[] for i in range(self.N)]
        self.edges = 0
        self.flag_node = len(self.node_list)

    def add_path(self, path: np.ndarray):
        np.append(self.paths, path, axis=0)
        np.append(self.pheromone, np.asarray[[0.4]], axis=0)

    def compute_2node(self, index1: int, index2: int) -> float:
        return np.sum(np.square(self.node_list[index1]['position'] - self.node_list[index2]['position']))

    def compute_ants_path(self, ants_connections: list):
        for connection in ants_connections:
            length = 0
            self.connections.append(connection)
            for path in connection:
                length += self.compute_2node(path[0], path[1])
            self.lengths = np.append(self.lengths, length)
        sort_index = np.argsort(self.lengths)
        self.lengths = np.sort(self.lengths)
        self.connections = [self.connections[i] for i in sort_index]

    def create_node(self, index: int, position: np.ndarray, real: bool):
        self.node_list[index] = {"position": position, "real": real}

    def new_artificial_node(self, index, cycle):
        center = np.asarray([0, 0])
        counter = 0
        for i in cycle:
            center += self.node_list[i]["position"]
            counter += 1
        center = center / 4
        self.create_node(index, center, False)

    # dfs function to find cycles in graph
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

    # consider the edges above certain pheromone level
    def addEdges(self, threshhold=0.1):
        connections = self.paths[self.paths > threshhold]
        self.graph = [[] for i in range(self.N)]
        self.edges = 0
        for connection in connections:
            self.edges += 1
            self.graph[connection[0]].append(connection[1])
            self.graph[connection[1]].append(connection[0])

    # Function to safe new cycles
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

    def add_new_pheromones(self, Q=1):
        for i, connection in enumerate(self.connections):
            for path in connection:
                if path[0] < path[1]:
                    index = np.where([path[0], path[1]] == self.node_list)
                else:
                    index = np.where([path[1], path[0]] == self.node_list)
                self.pheromone[index] += Q / self.lengths[i]

    def get_probability(self, ant_pos: int, alpha=1, beta=5):
        distances = np.array([[0]])
        pheromones = np.array([[0]])
        possible_nodes = np.array([[0]])
        for index, path in enumerate(self.paths):
            print(path)
            print(type(path))
            if ant_pos == path[0] or ant_pos == path[1]:
                distances = np.append(distances, np.array([[(1 / self.compute_2node(path[0], path[1])) ** alpha]]), axis=0)
                pheromones = np.append(pheromones, np.array([[self.pheromone[index] ** beta]]), axis=0)
            if ant_pos == path[0]:
                possible_nodes = np.append(possible_nodes, np.array([[path[1]]]), axis=0)
            elif ant_pos == path[1]:
                possible_nodes = np.append(possible_nodes, np.array([[path[0]]]), axis=0)
        print(possible_nodes)
        distances = distances[1:]
        pheromones = pheromones[1:]
        possible_nodes = possible_nodes[1:]
        components = distances * pheromones
        sum_up = np.sum(components, axis=0)
        probabilities = components / sum_up
        print(probabilities)
        possible_nodes = np.concatenate((possible_nodes, probabilities), axis=1)
        return possible_nodes

    # old version do not use this function below, use the one above
    """
        def get_possible_paths(self, ant_pos: int, alpha: int, beta = int):
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
    """

