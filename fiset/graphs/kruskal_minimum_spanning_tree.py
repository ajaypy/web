"""
Kruskal's MST
sort all the edges by weight
add them in increasing order, skip the one which causes loop

This is a Greedy Algorithm
"""

from collections import defaultdict

def find(subsets,node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets,subsets[node].parent)
    return subsets[node].parent

def union(subsets,u,v):

    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v
    else:
        subsets[u].parent = v
        subsets[v].rank += 1

class Graph:

    def __init__(self, vertices):

        self.V = vertices
        self.graph = []

    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])

    def union(self,parent,rank,u,v):
        u_root = self.find(parent,u)
        v_root = self.find(parent,v)

        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        elif rank[v_root] < rank[u_root]:
            parent[v_root] = u_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph,key = lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)


        while e < self.V - 1:
            u,v,w = self.graph[i]
            i += 1

            x = self.find(parent,u)
            y = self.find(parent,v)

            if x != y:
                e += 1
                result.append([u,v,w])
                self.union(parent, rank,x,y)

        for u,v,wt in result:
            print ("%d -- %d == %d" % (u,v,wt))




g = Graph(4)
g.add_edge(0,1,10)
g.add_edge(0,2,6)
g.add_edge(0,3,5)
g.add_edge(1,3,15)
g.add_edge(2,3,14)

g.kruskal_mst()
