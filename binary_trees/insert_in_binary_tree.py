"""
given a binary tree, insert a new node into it
the node currently doesn't exist in the tree

Inorder traversal of BST is an array sorted in ascending order

The successive entry is R->L->L..
The preceding entry is L->R->R..


# Delete node in a BST
1.the node is a leaf : just delete the node
2.the node has only a right child: replace the node with its right child
3.the node has only a left child: replace the node with its left child
4.the node has both left and right child: find its successor and replace with this node


https://leetcode.com/articles/delete-node-in-a-bst/
https://www.gontu.org/how-to-delete-node-in-a-binary-search-tree/#tabs-5035-0-1
"""

class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class bst:

    def __init__(self):
        self.root = None

    def insert_iterative(self,val):

        if not self.root:
            self.root = node(val)

        head = self.root
        while head:
            if val < head.val:
                if head.left:
                    head = head.left
                else:
                    head.left = node(val)
            elif val > head.val:
                if head.right:
                    head = head.right
                else:
                    head.right = node(val)
            else:
                return head

    def insert_recursive(self,root,val):


        if not root:
            root = node(val)
            if not self.root:
                self.root = root
            #print ("NRE ROOT222:",root, val)

        print ("=====ROOT222:",root, val)

        if val > root.val:
            root.right  = self.insert_recursive(root.right,val) 
        elif val < root.val:
            root.left = self.insert_recursive(root.left,val) 
        return root

    def traverse_in_order(self,root,res=[]):
        if not root:
            return None
        self.traverse_in_order(root.left,res)

        tmp = [root.val]
        if root.left:
            tmp.append(root.left.val)
        else:
            tmp.append(None)
        if root.right:
            tmp.append(root.right.val)
        else:
            tmp.append(None)
        res.append(tmp)
        #print (res,root)
        self.traverse_in_order(root.right,res)
        return (res)
    
    def traverse_pre_order(self,root,res=[]):
        if not root:
            return None
        tmp = [root.val]
        if root.left:
            tmp.append(root.left.val)
        else:
            tmp.append(None)
        if root.right:
            tmp.append(root.right.val)
        else:
            tmp.append(None)
        res.append(tmp)
        #print (res,root)

        self.traverse_pre_order(root.left,res)
        self.traverse_pre_order(root.right,res)

        return (res)
    
    def traverse_post_order(self,root,res=[]):
        if not root:
            return None
        self.traverse_post_order(root.left,res)
        self.traverse_post_order(root.right,res)
        tmp = [root.val]
        if root.left:
            tmp.append(root.left.val)
        else:
            tmp.append(None)
        if root.right:
            tmp.append(root.right.val)
        else:
            tmp.append(None)
        res.append(tmp)
        #print (res,root)
        return (res)
    
    def traverse_descending(self,root,res=[]):
        if not root:
            return None
        self.traverse_descending(root.right,res)
        tmp = [root.val]
        res.append(root.val)
        self.traverse_descending(root.left,res)
        if root.left:
            tmp.append(root.left.val)
        else:
            tmp.append(None)
        if root.right:
            tmp.append(root.right.val)
        else:
            tmp.append(None)
        #res.append(tmp)
        return (res)
    
    def print_level(self):
        if not self.root:
            return None
        node_map = {}
        root = self.root
        res = []

        cur_level = 0
        node_map[cur_level] = []
        node_map[cur_level].append(root)

        while node_map[cur_level]:
            tmp_res = []
            next_level = (cur_level + 1 )% 2
            node_map[next_level] = []
            for node in node_map[cur_level]:
                if node.left:
                    node_map[next_level].append(node.left)
                if node.right:
                    node_map[next_level].append(node.right)
                tmp_res.append(node.val)
            res.append(tmp_res)
            cur_level = next_level
        print (res)



    def get_node(self,val):

        head = self.root
        while head:
            if head.val == val:
                return head
            elif val < head.val:
                head = head.left
            else:
                head = head.right
        return None

    def get_successor(self,node):
        node = node.right
        while node.left:
            node = node.left
            print ("SUCC:", node.val)
        return node.val

    def get_predecessor(self,node):
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def delete_node_recursive(self,node, key):
        #1. find the node with the value
        # tree recusrions pass in and return nodes
        if not node:
            return None

        if key > node.val:
            node.right = self.delete_node_recursive(node.right,key)
        elif key < node.val:
            node.left = self.delete_node_recursive(node.left,key)
        else:
            if not (node.left or node.right):
                node = None
            elif (node.right):
                node.val = self.get_successor(node)
                node.right = self.delete_node_recursive(node.right,node.val)
            else:
                node.val = self.get_predcessor(node)
                node.left = self.delete_node_recursive(node.left,node.val)

        return node


vals = [51,20,70,15,32,91,11,21,101,121,81,55]
btree =  bst()
for val in vals:
    #print ("----BTREE ROOT:",btree.root)
    #btree.insert_recursive(btree.root,val)
    btree.insert_iterative(val)

print ("BTREE ROOT:",btree.root)
#print ("BTREE ROOT:",btree.root,"Val:",btree.root.val)
import pdb
#pdb.set_trace()

for val in vals:
    print (btree.get_node(val))

in_order = btree.traverse_in_order(btree.root)
print (in_order)

pre_order = btree.traverse_pre_order(btree.root)
print (pre_order)

post_order = btree.traverse_post_order(btree.root)
print (post_order)
btree.delete_node_recursive(btree.root, 51)

res1 = btree.traverse_pre_order(btree.root,[])
print (res1)

res1 = btree.traverse_in_order(btree.root,[])
print (res1)

res1 = btree.traverse_post_order(btree.root,[])
print (res1)

btree.print_level()
res1 =  btree.traverse_descending(btree.root,res=[])
print (res1)
