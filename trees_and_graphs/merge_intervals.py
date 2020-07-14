"""
Given a list of intervals, merge them
"""

# Connected Components
"""
1.iterate over all the components and collect all that overlap
2.merge the overlapping 
  The merge is recursive
3.use hashmap to keep trace of the overlapping components

Space:
    O(N ** 2)
Time:
    O(N ** 2)

"""
import collections
class merge_intervals_graph:

    def overlap(self,a,b):
        return a[0] <= b[1] and b[0] <= a[1]


    def build_graph(self,intervals):

        graph = collections.defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i+1,len(intervals)):
                if self.overlap(interval_i,intervals[j]):
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)

        return graph

    def merge_nodes(self,nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]


    def get_components(self,graph,intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        def mark_component_dfs(start):
            stack = [start]
            while stack:
                print (stack)
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        for interval in intervals:
            if tuple(interval) not in visited:
                mark_component_dfs(interval)
                comp_number += 1

        print ( nodes_in_comp,comp_number)
        return nodes_in_comp,comp_number


    def merge(self,intervals):
        graph = self.build_graph(intervals)
        print ( graph)
        nodes_in_comp,num_of_comps = self.get_components(graph,intervals)
        print ("COMPONENTS:",nodes_in_comp,num_of_comps)


        return [self.merge_nodes(nodes_in_comp[comp]) for comp in range(num_of_comps)]

intervals = [[1,3],[2,6],[8,10],[15,18]]
mig =  merge_intervals_graph()
g1 = mig.build_graph(intervals)
print (g1)
print (mig.merge(intervals))
# Sort and Merge 
"""
1.sort all intervals by starting time
2.merge the overlapping 

Space:
    O(N) or O(1)
Time:
    O(NlogN)
"""


class merge_intervals_sort:

    def merge(self, intervals):

        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1],interval[1])
        return merged

mis =  merge_intervals_sort()
print (mis.merge(intervals))
