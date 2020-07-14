"""
Given the output of the pre and in order traversals. Reconstruct the tree
Pre: first elemment if the root
In: root divides the traversal into left and rigth

take the first index in pre: that is the root
Get the index of that val in inorder. All elements to the left are the left subtree of that root



GENERAL THING ABT RECURSION of the BINARY TREE
current node is the root of the subtree

Get the root
then do the operation
find the left
find the right 
return the node

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(preorder,inorder):

    def helper(in_left = 0,in_right=len(inorder)):
        print ("in_left: %r, in_right: %r" % (in_left, in_right))

        nonlocal pre_idx
        if in_left == in_right:
            return None

        root_val = preorder[pre_idx]
        root = TreeNode(root_val)

        index = idx_map[root_val]

        pre_idx += 1

        # build left subtree: 
        # the left of the root is the root of the left subtree
        print ("LEFT")
        root.left = helper(in_left, index)
        # build right subtree: 
        # the right of the root is the root of the right subtree
        print ("RIGHT")
        root.right = helper(index+1,in_right)
        return root

    pre_idx = 0
    idx_map = {val:idx for idx,val in enumerate(inorder)}
    return (helper())


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
build_tree(preorder,inorder)
