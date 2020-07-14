"""
https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/

https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/tutorial/

https://www.geeksforgeeks.org/segment-tree-efficient-implementation/

A segment tree is a binary tree where each node represents an interval. Each node stores one or more 
properties of an interval which can be queried later


data be an array arr[] of size n
the root of the tree trr[0] represents all the elements in the arr[0:n]
each leaf of the tree represents one element in the array, arr[0], arr[1], ..., arr[n-1]

the internal nodes of the tree will represent the merged or the union result of their children nodes

the children of tree[i] are stored at tree[2*i+1] and tree[2*i+2]

for an array of size N
the segment tree will be 2*N with the arr as the leaf nodes
"""

# following builds tree with 1 as the root
class seg_tree_iterative:
    def __init__(self, arr):
        self.N = len(arr)
        self.arr = arr
        self.tree = [0]* (2 * self.N)

    def build_seg_tree_iterative(self):
        
        #insert the leaf nodes
        for i in range(self.N):
            self.tree[self.N+i] = self.arr[i]
    
        #build the tree by calculating parents
        for i in range(self.N-1,0,-1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
    
        return self.tree
    
    
    def update_seg_tree_iterative(self,p, value):
            self.tree[p + self.N] = value
            i = p + self.N
            while i > 1:
                self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
                i >>= 1
    def query(self,l,r):
        print ("IN--------:",l,r)

        res = 0

        l += self.N
        r += self.N

        print ("NORM------:",l,r)
        print (self.tree[l],self.tree[r])

        while l < r:
            print ("LOOP------:",l,r)
            # if l is odd , it needs to be added separatley
            if (l & 1):
                res += self.tree[l]
                l += 1
            # as r is not included, if r is odd then its peer needs to be added
            if (r & 1):
                r -= 1
                res += self.tree[r]

            l >>= 1
            r >>= 1
        return res


# following builds tree with 0 as the root
def build_seg_tree_recursive(arr,tree_index,lo,hi):
    print ("IN  :", tree_index,lo,hi)

    if (lo == hi):
        tree[tree_index] = arr[lo]
        return

    mid = lo + (hi - lo)//2
    build_seg_tree_recursive(arr,2 * tree_index + 1, lo, mid)
    build_seg_tree_recursive(arr,2 * tree_index + 2, mid+1, hi)


    tree[tree_index] = tree[2* tree_index + 1] + tree[2*tree_index + 2]

tree = [0]* 32
print (tree)
arr = [ 18, 17, 13, 19, 15, 11, 20, 12, 33, 25 ,26]
build_seg_tree_recursive(arr,0,0,len(arr)-1)

#for i , ele in enumerate(tree):
#    print (i, ele)
st  = seg_tree_iterative(arr)
st.build_seg_tree_iterative()
for i , ele in enumerate(st.tree):
    print (i, ele)

st.update_seg_tree_iterative(4,67)
for i , ele in enumerate(st.tree):
    print (i, ele)

st.update_seg_tree_iterative(4,6)
for i , ele in enumerate(st.tree):
    print (i, ele)
#print (len(st.tree))
#for i in range(1,len(st.tree)):
#    print (i, (2*i), (2 * i + 1))

print (st.query(7,10))
#print (st.tree[7])
#print (st.tree[10])
#print (st.N)
