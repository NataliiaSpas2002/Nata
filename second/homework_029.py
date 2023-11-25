# Topic 29
# Task 1

# The defaultdict(list) is used to initialize the graph with default values of an empty list for each vertex.
# This is convenient because it allows you to append edges to vertices without explicitly checking
# if the vertex is already in the graph.

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    # to add an edge between two vertices u and v in the graph,
    # this method is responsible for building the graph by adding edges between vertices.
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # We explore the graph starting from a given vertex v, marking visited vertices,
    # and pushing the vertices onto a stack in the order they are visited.

    def depth_first_search(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.depth_first_search(i, visited, stack)

        stack.append(v)

    # creates a new instance of the Graph class
    # with the same number of vertices as the original graph.
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)

        return g

    def fill_order(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.fill_order(i, visited, stack)

        stack.append(v)

    def strongly_connected_components(self):
        stack = []
        visited = [False] * (self.V)

        for i in range(self.V):
            if not visited[i]:
                self.depth_first_search(i, visited, stack)

        new_graph = self.transpose()

        visited = [False] * (self.V)

        strongly_connected_components = []

        while stack:
            i = stack.pop()
            if not visited[i]:
                component = []
                new_graph.fill_order(i, visited, component)
                strongly_connected_components.append(component)

        return strongly_connected_components


# Example usage:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

print("Strongly Connected Components:")
print(g.strongly_connected_components())



