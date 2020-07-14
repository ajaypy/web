"""
schedule classes based on pre-requisiotns
https://leetcode.com/articles/course-schedule-ii/
"""

from collections import defaultdict,deque

"""
adj_lists: [(0, [1, 2]), (1, [3]), (2, [3])]
Solution based on finding cyclces in graph
If cycles are present in graph , no solution is possible
"""
class Solution_Dfs:

    WHITE = 1
    GRAY = 2
    BLACK = 3


    def __init__(self, num_courses, pre_req):
        self.num_courses = num_courses
        self.pre_req = pre_req

    def find_order(self, num_courses, pre_req):

        adj_list = defaultdict(list)

        for dest,src in pre_req:
            adj_list[src].append(dest)

        print (adj_list.items())
        topological_sorted_order = []
        is_possible = True
        
        # By default all vertices are WHITE

        color = {k: Solution_Dfs.WHITE for k in range(num_courses)}
        def dfs(node):
            nonlocal is_possible

            if not is_possible:
                return

            #start recursion
            color[node] = Solution_Dfs.GRAY
            print ("Node :%r  %r" % (node,color.items()))

            #Traverse on neighboring vertices
            if node in adj_list:
                for nbr in adj_list[node]:
                    if color[nbr] == Solution_Dfs.WHITE:
                        dfs(nbr)
                    elif color[nbr] == Solution_Dfs.GRAY:
                        is_possible = False

            color[node] = Solution_Dfs.BLACK
            topological_sorted_order.append(node)

        for vertex in range(num_courses):
            print ("VERTEX :", vertex)
            if color[vertex] == Solution_Dfs.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []


class Solution_In_Degree:

    def __init__(self, num_courses, pre_req):
        self.num_courses = num_courses
        self.pre_req = pre_req

    def find_order(self, num_courses, pre_req):

        adj_list = defaultdict(list)
        indegree = {}

        for dest,src in pre_req:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest,0) + 1


        # Queue for nodes with 0 in-degree
        zero_q = deque([k for k in range(num_courses) if k not in indegree])

        topological_sorted_order = []

        while zero_q:
            vertex = zero_q.popleft()
            topological_sorted_order.append(vertex)

            if vertex in adj_list:
                for nbr in adj_list[vertex]:
                    indegree[nbr] -= 1 
                    if indegree[nbr] == 0:
                        zero_q.append(nbr)

        return topological_sorted_order if len(topological_sorted_order) == num_courses else []

num_courses = 4
pre_req = [[1,0],[2,0],[3,1],[3,2]]
sol = Solution_Dfs(num_courses,pre_req)
ret_val = sol.find_order(num_courses,pre_req)
print ("Order",ret_val)

sol = Solution_In_Degree(num_courses,pre_req)
ret_val = sol.find_order(num_courses,pre_req)
print ("Order",ret_val)
