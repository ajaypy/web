"""
Dijkstra's SPF
we have a set of nodes and a array of distance from the src
A set of nodes already found with the shortest path and another set undetermined
Can be visited and not visited

at each step update the distance of the nearest node among the not visited
and visit its neighbors

dist[] : array of the distance of each node from src
visited[] : array of nides that are visited


initialize dist[] with infinity
Optimize at every level. At every level update the distance wrt 
the nearest node and mark the nearest node as visited

current node = Src.
for all nbrs of current_node:
    if dist of current_node + distance to nbr > current_dist of node:
    replace it
    mark the current node as  visited

Adjacency Matrix
https://medium.com/cantors-paradise/dijkstras-shortest-path-algorithm-in-python-d955744c7064
https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
"""
import sys
class Graph_adj_matrix:

    def __init__(self, vertices):

        self.V = vertices
        self.graph = [[ 0 for col in range(self.V)] for row in range(self.V)]


    def print_sol(self,dist):
        for node in range(self.V):
            print(node," : ", dist[node])

    # find node with min_d and not yet visited
    def min_distance(self,dist, spt_set):

        min_d = float('inf')
        print (dist)
        print (spt_set)
        for v in range(self.V):
            if dist[v] < min_d and spt_set[v] == False:
                min_d = dist[v]
                min_index = v
        return min_index

    # find the shortest distance to all nodes from the src
    def dijkstra(self,src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for count in range(self.V):
            u = self.min_distance(dist,spt_set)
            print ("MIN_INDEX:", u)
            spt_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and spt_set[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.print_sol(dist)

g = Graph_adj_matrix(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

for row in g.graph:
    print (row)
g.dijkstra(0)
