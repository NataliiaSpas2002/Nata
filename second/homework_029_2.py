# Topic 29
# Task 2

import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, start, end):
        priority_queue = [(0, start)]
        visited = set()

        while priority_queue:
            (current_distance, current_vertex) = heapq.heappop(priority_queue)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            if current_vertex == end:
                return current_distance

            for neighbor, weight in self.graph[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (current_distance + weight, neighbor))

        return float('inf')


g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 5)
g.add_edge(1, 2, 3)
g.add_edge(2, 3, 4)
g.add_edge(2, 4, 7)


shortest_distance = g.dijkstra(0, 3)
print(shortest_distance)








