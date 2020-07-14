"""
Threaded binary tree

Traverse in-order

While Left go to left
add curr
Go to right
"""

def tree_traversal_with_stack(root):
    n_stack = []
    r_stack = []

    curr = root

    while  curr and n_stack:
        while curr.left:
            n_stack.append(curr)
            curr = curr.left

        curr = n_stack.pop()
        r_stack.append(curr.val)
        curr = curr.right




def threaded_binary_tree(root):

    curr = root
    while curr:
        if curr.left:
            L = curr.left
            tmp = curr.left
            while tmp.right:
                tmp = tmp.right
            tmp.right = curr
            tmp = curr
            curr.left = None
            curr = L


