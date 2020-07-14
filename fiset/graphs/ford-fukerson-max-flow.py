"""
given a graph, find the max flow possibe between the Source (S) and Sink (T)

1. Start with initial flow as 0
2. While there is a augmenting parent from S to T:
    add this parent-flow to the flow
3. Return flow

The greedy will find the best for given case, but we need to undo if need be

http://theory.stanford.edu/~tim/w16/l/l1.pdf
https://www.geeksforgeeks.org/max-flow-problem-introduction/
https://www.hackerearth.com/practice/algorithms/graphs/maximum-flow/tutorial/
https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
https://cs.stackexchange.com/questions/55041/residual-graph-in-maximum-flow
http://cseweb.ucsd.edu/~kube/cls/100/Lectures/lec12.netflow/lec12-1.html#pgfId-968511
http://cseweb.ucsd.edu/~kube/cls/100/Lectures/
"""

from collections import defaultdict

class Graph:
    
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.row = len(graph)


    def bfs(self, s, t,parent):
        print ("---------------------- -------------------")
        for i in range(self.row):
            print (self.graph[i])
        print ("---------------------- -------------------")

        visited = [False] * (self.row)

        # create a queue for BFS
        queue = []
        path = []

        queue.append(s)
        path.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            print ("U: %r, " % (u))
            for ind,val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    print ("ind: %r, val: %r" % (ind, val))
                    queue.append(ind)
                    visited[ind] = True
                    path.append(ind)
                    parent[ind] = u

        print ("PARENT:",parent)
        print ("PATH:",path)
        if visited[t] == True:
            print ("Reached T")
            return True
        return False

    def max_flow(self, source, sink):



        # parent found by bfs
        parent = [-1] * self.row

        #initialy 0 flow
        max_flow = 0


        while self.bfs (source, sink, parent):
            path_flow = float("Inf")
            s = sink

            while ( s!= source ):
                path_flow = min(path_flow,self.graph[parent[s]][s])
                s = parent[s]

            print ("path_flow ", path_flow)
            max_flow += path_flow

            #update residual capacities and reverse edges along the path
            v = sink
            while v!= source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow


graph = [[0, 16, 13, 0, 0, 0], 
        [0, 0, 10, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 4], 
        [0, 0, 0, 0, 0, 0]]

g = Graph(graph)
source = 0
sink = 5

print ("Max flow = %r" % g.max_flow(source,sink)) 
