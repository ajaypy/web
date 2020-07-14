"""
graph as an adjacency list
"""

graph = {
        'A': ['B','C'],
        'B': ['D','E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
        }
visited = set()

def dfs_graph_1(visited,graph,node):
    if node not in visited:
        print (node)
        visited.add(node)
        for nbr in graph[node]:
            dfs_graph_1(visited,graph,nbr)

dfs_graph_1(visited,graph,'A')

