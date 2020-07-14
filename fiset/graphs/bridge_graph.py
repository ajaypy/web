"""
find if there is a bridge in a graph
a bridge will split the graph into two if its removed

#remove an edge ,
# starting from one vertex of the edge,traverse the adjacency matrix
# all the vertices and see if there still exits another way to reach the other end
# if still exists another path to other end, this edge is not a bridge
"""
from collections import defaultdict
from collections import deque
class Edge:
    def __init__(self, u,v):
        self.u = u
        self.v = v

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.E = 0
        self.graph = defaultdict(list)
        self.Edges = []

    def add_adj(self, u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def add_edge(self, u,v):
        self.Edges.append(Edge(u,v))
        self.E += 1

    def get_nbr_index(self,u,v):
        for x in range(len(self.graph[u])):
            if self.graph[u][x] == v:
                return x
        return -1

    def find_bridge(self):
        bridges = []

        for i in range(self.E):
            visited = [False] * self.V
            has_bridge = True
            node_q = deque()
            u = self.Edges[i].u
            v = self.Edges[i].v
            index_v = self.get_nbr_index(u,v)
            index_u = self.get_nbr_index(v,u)
            self.graph[u][index_v] = -1 
            self.graph[v][index_u] = -1 
            print ("Edge:", u,v)
            print ("Node U:",u,self.graph[u])
            print ("Node V:",v,self.graph[v])
            node_q.append(u)
            while node_q:
                print ("Stack top:", node_q)
                cur = node_q.popleft()
                if cur == -1:
                    continue

                if cur == v:
                    print ("CURR: ", cur)
                    has_bridge = False
                    break

                visited[cur] = True
                for node in self.graph[cur]:
                    if node != -1 and visited[node] == False:
                        node_q.append(node)
            if has_bridge:
                bridges.append([u,v])
            self.graph[u][index_v] = v
            self.graph[v][index_u] = u
        return bridges


g3 = Graph(7)
g3.add_edge(0, 1)
g3.add_edge(0, 2)
g3.add_edge(1, 3)
g3.add_edge(1, 2)
g3.add_edge(2, 3)
g3.add_edge(0, 4)
g3.add_edge(4, 5)
g3.add_edge(4, 6)
g3.add_edge(6, 5)
g3.add_edge(6, 2)

g3.add_adj(0, 1)
g3.add_adj(0, 2)
g3.add_adj(1, 3)
g3.add_adj(1, 2)
g3.add_adj(2, 3)
g3.add_adj(0, 4)
g3.add_adj(4, 5)
g3.add_adj(4, 6)
g3.add_adj(6, 5)
g3.add_adj(6, 2)

print (g3.E)
for ele in g3.Edges:
    print (ele.u, ele.v)
for ele in g3.graph:
    print (ele,g3.graph[ele])

bridges = g3.find_bridge()
print (bridges)
