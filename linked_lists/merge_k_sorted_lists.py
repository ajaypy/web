"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

https://leetcode.com/articles/merge-k-sorted-list/
"""
class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None

#1 Brute Force
"""
Traverse all the linked lists and collect the values of the nodes into an array.
Sort and iterate over this array to get the proper value of nodes.
Create a new sorted linked list and extend it with the new nodes.

Time:
iteration of the linked lists and inserting into array O(N)
sorting algo O(N log N)
iterating for creating the new list O(N)

Space:
    Sorting O(N)
    New Lisnked List O(N)
    Array O(N)
"""
class brute_force_sol:
    def __init__(self, lists):

        self.lists = lists
        self.nodes = []

        self.head = self.point = ListNode(0)

    def merge_k_sorted(self, lists):
        for l in self.lists:
            while l:
                self.nodes.append(l.val)
                l = l.next

        for x in sorted(self.nodes):
            self.point.next = ListNode(x)
            self.point = self.point.next

        return self.head.next

#2 Compare Individual Elements
"""
Algorithm

Compare every k nodes (head of every linked list) and get the node with the smallest value.
Extend the final sorted linked list with the selected nodes.


If lots of lists with less individual elemets, this is similar to the Brute Force
"""

#3 Use Priority Queue to sort
"""
Use a priority queue to sort the values, rather than list

Implements option 2 using priority queue

O(N log k) : k number of linked lists

Space:
    O(N) new linked list
    O(k) Priority Queue
"""

from Queue import PriorityQueue


class pq_sol:
    def __init__(self, lists):

        self.lists = lists
        self.nodes = []
        self.head = self.point = ListNode(0)
        self.q = PriorityQueue()

    def merge_k_sorted(self, lists):
        for l in self.lists:
            if l:
                q.put(l.val,l)

        while not q.empty():
            val,node = q.get()
            self.point.next = ListNode(val)
            self.point = self.point.next
            node = node.next
            if node:
                q.put((node.val.node))
        return head.next

