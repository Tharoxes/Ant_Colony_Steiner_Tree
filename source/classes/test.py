import numpy as np

"""
class test:
    def __init__(self, list):
        self.list = list
        self.n = len(list)

dict = {
    1: "h",
    2: "a",
}
a = test(dict)
print(a.n)
a.list[4] ="l"
print(a.n)
print(a.list)
"""

arr1 = np.array([[1], [2]])

arr2 = np.array([[5], [6]])

arr = np.concatenate((arr1, arr2), axis=1)

distances = np.array([[0]])
distances = np.append(distances, np.array([[5]]), axis=0)
distances = np.append(distances, np.array([[6]]), axis=0)
distances = distances[1:]

d = np.array([[0]])
d = np.append(d, np.array([[3]]), axis=0)
d = np.append(d, np.array([[4]]), axis=0)
d = d[1:]

#print(distances)
#print(d)
bla = np.concatenate((distances, d), axis=1)
#print(bla)
#print(bla[1, 0])

dict = {
    1: "h",
    2: "a",
}

#print(list(dict)[-1])
a = np.array([1, 2])
#print(np.array([1, 2]))
#print(type(a))

a = [1, 2]
a.append(3)
print(a)

a = np.array([3, 4])
a = np.append(a, 5)
print(a)
print(type(np.sum(a)))

N = 15
# print(np.sum(np.square(np.array([4, 2])-np.array([2, 3]))))

j = 0
a = [1, 2, 3, 4, 5, 9]
for i in a[j:]:
    # print(i)
    j += 1

a = [1, 2, 3, 4, 5, 9, 7, 8]
for i in a[j:]:
    # print(i)
    j += 1

# variables to be used
# in both functions
graph = [[] for i in range(N)]
cycles = [[] for i in range(N)]


# Function to mark the vertex with
# different colors for different cycles
def dfs_cycle(u, p, color: list,
              mark: list, par: list):
    global cyclenumber

    # already (completely) visited vertex.
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
        # print("cur is ", cur)

        # backtrack the vertex which are
        # in the current cycle thats found
        while cur != u:
            cur = par[cur]
            # print(cur)
            mark[cur] = cyclenumber

        return
    # print(u, " ", p)
    par[u] = p

    # partially visited.
    color[u] = 1

    # simple dfs on graph
    for v in graph[u]:

        # if it has not been visited previously
        if v == par[u]:
            continue
        dfs_cycle(v, u, color, mark, par)

    # completely visited.
    color[u] = 2


# add the edges to the graph
def addEdge(u, v):
    graph[u].append(v)
    graph[v].append(u)


# Function to print the cycles
def printCycles(edges, mark: list):
    # push the edges that into the
    # cycle adjacency list
    for i in range(1, edges):
        if mark[i] != 0:
            cycles[mark[i]].append(i)

    # print all the vertex with same cycle
    for i in range(1, cyclenumber + 1):
        # print(cycles[i])
        """
        # Print the i-th cycle
        print("Cycle Number %d:" % i, end=" ")
        for x in cycles[i]:
            print(x, end=" ")
        print()

        """


# Driver Code
if __name__ == "__main__":
    # add edges
    addEdge(1, 2)
    addEdge(2, 3)
    addEdge(3, 4)
    addEdge(4, 6)
    addEdge(4, 7)
    addEdge(5, 6)
    addEdge(3, 5)
    addEdge(7, 8)
    addEdge(6, 10)
    addEdge(5, 9)
    addEdge(10, 11)
    addEdge(11, 12)
    addEdge(11, 13)
    addEdge(12, 13)

    # arrays required to color the
    # graph, store the parent of node
    color = [0] * N
    par = [0] * N

    # mark with unique numbers
    mark = [0] * N
    # print(type(mark))

    # store the numbers of cycle
    cyclenumber = 0
    edges = 14

    # call DFS to mark the cycles
    dfs_cycle(1, 0, color, mark, par)

    # function to print the cycles
    printCycles(edges, mark)

    # print(graph)

    a = np.array([1, 2, 3, 6, 1, 2, 4])
    b = np.array([[2], [2], [3], [3], [4], [4], [5]])
    c = a > 1
    # print(b[c])
