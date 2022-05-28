# todo: map class can track and save the routes as .csv or something else
import numpy as np
# import node


class Map:
    def __init__(self, node_list: dict, paths: np.ndarray, pheromones: np.ndarray):
        self.N = 300
        self.node_list = node_list # {1: x,y, , 2, 3, etc.} dict with np.ndarray and bool
        self.paths = paths # [[1, 2], [3, 2], etc.] [index, index] always smaller index at the front
        self.pheromone = pheromones # relativ values 2d array
        self.probability = []
        self.connections = list()
        self.lengths = np.asarray([])
        self.graph = [[] for i in range(self.N)]
        self.cycles = list()
        self.edges = 0
        self.cyclenumber = 0
        self.flag_node = len(self.node_list)

    def add_path(self, path: np.ndarray):
        self.paths = np.append(self.paths, path, axis=0)
        #print(self.pheromone)
        self.pheromone = np.append(self.pheromone, np.array([[0.4]]), axis=0)

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

    def create_paths_and_pheromones(self, pheromone=0.4):
        for x in list(self.node_list)[:-1]:
            #print(x)
            #print(list(self.node_list)[-1])
            self.add_path(np.array([[x, list(self.node_list)[-1]]]))

    def new_artificial_node(self, index, cycle):
        center = np.array([0, 0])
        counter = 0
        for i in cycle:
            #print(i)
            center = np.add(center, self.node_list[i]["position"])
            #print(self.node_list[i]["position"])
            counter += 1
        center = center / counter
        #print("Here: ", center)
        self.create_node(index, center, False)
        self.create_paths_and_pheromones()

    # dfs function to find cycles in graph
    def dfs_cycles(self, u, p, color: list, mark: list, par: list):
        """

        @param u: int; actual node
        @param p: int, parent node of u
        @param color: list int, colorization for visited nodes
        @param mark: list int, marked nodes for a certain cycle
        @param par: list of int, parents of all nodes
        @return:
        """
        if color[u] == 2:
            return

        # seen vertex, but was not
        # completely visited -> cycle detected.
        # backtrack based on parents to
        # find the complete cycle.
        if color[u] == 1:
            self.cyclenumber += 1
            cur = p
            mark[cur] = self.cyclenumber

            # backtrack the vertex which are
            # in the current cycle thats found
            while cur != u:
                cur = par[cur]
                mark[cur] = self.cyclenumber

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
        """

        @param threshhold: updated the list of considered edges above a certain pheromone level
        """
        self.graph = [[] for i in range(self.N)]
        self.edges = 0
        for index, pheromone in enumerate(self.pheromone):
            if pheromone > threshhold:
                self.edges += 1
                self.graph[self.paths[index, 0]].append(self.paths[index, 1])
                self.graph[self.paths[index, 1]].append(self.paths[index, 0])

    # Function to safe new cycles
    def safe_Cycles(self, mark: list, N):
        """

        @param edges: list of int; number of the edges
        @param mark: list; marked nodes in a cycle
        """
        new_cycles = [[] for i in range(N)]
        #print(type(new_cycles))
        for i in range(1, self.edges):
            if mark[i] != 0:
                new_cycles[mark[i]].append(i)
            # print(new_cycles)

        new_cycles = [i for i in new_cycles if len(i) != 0]

        for j in new_cycles:
            if len(j) < 3:
                continue
            j.sort()
            if j not in self.cycles:
                self.cycles.append(j)

    def evaporate(self, evaporation=0.9): # how to update new connections with low costs
        """

        @rtype: rate of pheromones vaporization from t to t+1
        """
        for pheromone in self.pheromone:
            pheromone *= evaporation

    def add_new_pheromones(self, Q=1):
        """

        @rtype: updates the pheromones by adding Q / L_k
        """
        for i, connection in enumerate(self.connections):
            for path in connection:
                if path[0] < path[1]:
                    index = np.where([path[0], path[1]] == self.node_list)
                else:
                    index = np.where([path[1], path[0]] == self.node_list)
                self.pheromone[index] += Q / self.lengths[i]

    def get_probability(self, ant_pos: int, alpha=1, beta=5):
        """

        @param ant_pos: int; position of the ant on Node xy
        @param alpha: float; from the paper to calculate the probability and give weights on pheromones
        @param beta: float; from the paper to calculate the probability and give weights on desirability
        @return: np.ndarray, shape(possible nodes, probabilities) (possible node: int, probability 0-1);
        """
        ant_pos = int(ant_pos)
        # print(ant_pos)
        distances = np.array([[0]])
        pheromones = np.array([[0]])
        possible_nodes = np.array([[0]])
        for index, path in enumerate(self.paths):
            if ant_pos == path[0] or ant_pos == path[1]:
                distances = np.append(distances, np.array([[(1 / self.compute_2node(path[0], path[1])) ** alpha]]), axis=0)
                pheromones = np.append(pheromones, np.array([self.pheromone[index] ** beta]), axis=0)
            if ant_pos == path[0]:
                possible_nodes = np.append(possible_nodes, np.array([[path[1]]]), axis=0)
            elif ant_pos == path[1]:
                possible_nodes = np.append(possible_nodes, np.array([[path[0]]]), axis=0)
        distances = distances[1:]
        pheromones = pheromones[1:]
        possible_nodes = possible_nodes[1:]
        components = distances * pheromones
        sum_up = np.sum(components, axis=0)
        probabilities = components / sum_up
        possible_nodes = np.concatenate((possible_nodes, probabilities), axis=1)
        #print(possible_nodes)
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

