"""
Find articulation points in a graph
"""

from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def add_edge(self, u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    """
    a recursive function that find articulation points
    using DFS traversal
    u ---> the vertex to be visited next
    visited[] ---> keeps track of visited vertices
    dic[] ---> discovery time of the node
    parent[] ---> parent in the DFS tree
    ap[] ---> store articulation points
    """
    def ap_utils(self, par,visited,ap,parent,low,disc):

        children = 0
        visited[par] = True

        disc[par] = self.Time
        low[par] = self.Time
        self.Time += 1

        for v in self.graph[par]:

            if visited[v] == False:
                parent[v] = par
                children += 1
                self.ap_utils( v,visited,ap,parent,low,disc)
                low[par] = min(low[par], low[v])

                if parent[par] == -1 and children > 1:
                    ap[par] = True

                if parent[par] != -1 and low[v] >= disc[par]:
                    ap[par] = True
            elif v != parent[par]:
                low[par] = min(low[par], disc[v])

    def ap(self):
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)
        ap = [False] * (self.V)

        for i in range(self.V):
            if visited[i] == False:
                self.ap_utils(i,visited,ap,parent,low,disc)
        print ("VISITED:", visited)
        print ("Parent:", parent)
        print ("DISC:", disc)
        print ("LOW:", low)
        for index, value in enumerate(ap):
            if value == True:
                print (index)
g1 = Graph(5)
g1.add_edge(1, 0)
g1.add_edge(0, 2)
g1.add_edge(2, 1)
g1.add_edge(0, 3)
g1.add_edge(3, 4)

print ("AP in G1")
r = g1.ap()

g2 = Graph(4)
g2.add_edge(1, 0)
g2.add_edge(2, 1)
g2.add_edge(3, 2)

print ("AP in G2")
r = g2.ap()

g3 = Graph(7)
g3.add_edge(0, 1)
g3.add_edge(1, 2)
g3.add_edge(2, 0)
g3.add_edge(1, 3)
g3.add_edge(1, 4)
g3.add_edge(1, 6)
g3.add_edge(3, 5)
g3.add_edge(4, 5)

print ("AP in G3")
r = g3.ap()



