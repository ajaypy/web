"""
given a graph, find the hamilton path
"""

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(self.V)] for row in range(self.V)]

    def update_graph(self, adj):
        for i in range(self.V):
            self.graph[i] = adj[i]

    def check_vertex(self, v, pos, path):

        # check if vertex v can be added at position 'pos'
        # check if the given vertex has a edge to the vertex in previous position
        # and if the vertex is already in the path

        if self.graph[path[pos-1]][v] == 0:
                return False
        for vertex in path:
            if vertex == v:
                return False
        return True
        
    def ham_cycle_util(self, path, pos):

        if pos == self.V:
            if self.graph[path[pos-1]][path[0]] == 1:
                return True
            else:
                return False

        # check if any of the nodes can occupy the position
        for v in range(1, self.V):
            if self.check_vertex(v,pos, path):
                path[pos] = v

                if self.ham_cycle_util(path,pos+1):
                    return True

                path[pos] = -1

        return False

    def ham_cycle(self):

        path = [-1] * self.V

        path[0] = 0

        if self.ham_cycle_util(path,1) == False:
            print ("NO Soution")
            return False

        for vertex in path:
            print (vertex, end = " ")
        print (path[0], "\n")

g1 = Graph(5)
adj = [ [0, 1, 0, 1, 0], 
         [1, 0, 1, 1, 1],  
         [0, 1, 0, 0, 1],
         [1, 1, 0, 0, 1],  
         [0, 1, 1, 1, 0], ]

g1.update_graph(adj)
g1.ham_cycle()
