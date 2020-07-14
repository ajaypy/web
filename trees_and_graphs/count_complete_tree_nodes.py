"""
Given a complete binary tree, count the number of nodes.
In a complete binary tree, every level except the last is completley filled
https://leetcode.com/articles/count-complete-tree-nodes/


#1 find the depth of the tree
#2 find the right most node in that level

1. Use binary search to construct the sequence of moves
Return 0 if the tree is empty.

2. Compute the tree depth d.

Return 1 if d == 0.

3. The number of nodes in all levels but the last one is 2^d - 1
 The number of nodes in the last level could vary from 1 to 2^d. 
 Enumerate potential nodes from 0 to 2^d - 1 and perform the binary search 
 by the node index to check how many nodes are in the last level. Use the 
 function exists(idx, d, root) to check if the node with index idx exists.

Use binary search to implement exists(idx, d, root) as well.

Return 2^d - 1 + the number of nodes in the last level.
https://leetcode.com/articles/count-complete-tree-nodes/
"""

class Solution:

    def compute_depth(self, node):
        """
        return tree depth in O(d) time
        """

        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx, d, node):
        """
        Last level nodes are enumerated from 0 to 2**d -1
        Return True if last level node idx exists
        Binary search with O(d) complexity
        """

        left,right = 0, 2**d -1
        for _ in range(d):
            pivot = left + (right  - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def count_nodes(self, root):
        if not root:
            return 0

        d = self.compute_depth(root)
        if d == 0:
            return 1

        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1


        return (2**d - 1) + left

