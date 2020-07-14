"""
graph with adjacncy lists and 0-1 priority
"""

from sys import maxsize as INT_MAX
from collections import deque
class edge:
    def __init__(self,to, weight):
        self.to = to
        self.wt = weight

#graph as nodes and edges. 
# edge has two nodes, from and to and weight
# the edge is held by the source node array 
V = 9
nodes = [0] * V
for i in range(V):
    nodes[i] = []

def add_edges(u,v,wt):
    nodes[u].append(edge(v, wt))


# find distance from a src node
def zero_one_bfs(src):

    dist = [0] * V
    for i in range(V):
        dist[i] = INT_MAX

    Q = deque()
    dist[src] = 0
    Q.append(src)

    while Q:
        v = Q.popleft()

        for i in range(len(nodes[v])):
            if (dist(nodes[v][i].to] > dist[v] + nodes[v][i].wt):
                dist[edges[v][i].to] = dist[v] + nodes[v][i].wt:wq




