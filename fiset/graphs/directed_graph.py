"""
given a graph, print all paths between a source and destination

with Adjacency list:
   if the adj entry is made to only one node, it becomes a directed
   the adj entry has to be added to both nodes, to make it undirected

Find components:

"""

from collections import defaultdict

class Subset:
    def __init__(self,parent,rank):
        self.parent = parent
        self.rank = rank

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

def union(subsets,u,v):
class Graph:

    def __init__(self, vertices):

        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    # this assumes no cycle
    def get_all_path_rec(self,u,d,visited,path,all_paths):
        print(u,d,visited,path,all_paths)
        visited[u] = True
        path.append(u)

        if u == d:

            tmp = [x for x in path]
            all_paths.append(tmp)
            print (path)
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.get_all_path_rec(i,d,visited,path,all_paths)
        # once you have visited all nbrs backtracking to get all the paths
        path.pop()
        visited[u] = False


    def print_all_paths_rec(self,s,d):

        visited = [False]*(self.V)
        path = []
        all_paths = []
        self.get_all_path_rec(s,d,visited,path,all_paths)

        for ele in all_paths:
            print ("ELE --:", ele)

    def get_not_visited_index(self,visited):

        for i in range(len(visited)):
            if not visited[i]:
                return i
        return -1


    def get_all_components(self):
        visited = [False]*(self.V)
        components = []


        node = self.get_not_visited_index(visited)
        while node != -1:
            path = []
            stack = []
            stack.append(node)
            while stack:
                cur = stack.pop()
                if visited[cur]:
                    continue
                visited[cur] = True
                path.append(cur)
                for nbr in self.graph[cur]:
                    stack.append(nbr)
            components.append(path)
            node = self.get_not_visited_index(visited)
        print ("COMPONENTS ------------")
        for ele in components:
            print (ele)

    def is_cyclic(self,v,visited,rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for nbr in self.graph[v]:
            if visited[nbr] == False:
                if self.is_cyclic(nbr,visited,rec_stack) == True:
                    return True
            elif rec_stack[nbr] == True:
                    print (rec_stack)
                    return True

        rec_stack[v] = False

    def graph_has_cycle(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.is_cyclic(node,visited,rec_stack) == True:
                    return True
        return False

    def is_cycle_graph_union_join(self):

        subsets = []

        for u in range(self.V):
            subsets.append(Subset(u,0))

        for u in self.graph:

            u_rep = find(subsets,u)

            for v in self.graph[u]:
                v_rep = find(subsets,v)

                if u_rep == v_rep:
                    return True
                else:
                    union(subsets,v_rep,v_rep)


g = Graph(9)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(2,0)
g.add_edge(2,1)
g.add_edge(1,3)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(1,5)
g.add_edge(5,3)
g.add_edge(6,7)
g.add_edge(7,8)
s = 1
d = 0
g.print_all_paths_rec(s,d)
g.get_all_components()
print ("Has cycle: ", g.graph_has_cycle())
