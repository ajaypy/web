"""
implement union_find using an array
https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/tutorial/
"""

class union_find:
    def __init__(self,arr):
        self.arr = arr
        # assign each indexmen to its own set
        for i in range(len(arr)):
            arr[i] = i

    # find if the indexments A and B are connected
    def find(self,A,B):
        if self.arr[A] == self.arr[B]:
            return True
        return False

    # add all entries of group A to another group B
    def union(self,A,B):
        temp = self.arr[A]
        for i in range(len(self.arr)):
            if self.arr[i] == temp:
                self.arr[i] = self.arr[B]


class union_find_opt:
    def __init__(self,arr):
        self.arr = arr
        # assign each indexmen to its own set
        for i in range(len(arr)):
            arr[i] = i

    # find root of an indexment 
    def root(self,index):
        while self.arr[index] != index:
            index = self.Arr[index]
        return index

    # union of two by updating the root
    def union(self,A,B):
        root_a = self.root(A)
        root_b = self.root(B)
        self.arr[root_a] = root_b

    # find: if two indexments have same root,they are connected
    def find(self,A,B):

        if self.root(A) == self.root(B):
            return True
        return False

# have an extra array to store the size of each group
class union_find_wt:
    def __init__(self,arr):
        self.arr = arr
        self.size = []
        # assign each indexmen to its own set
        for i in range(len(arr)):
            arr[i] = i
            self.size.append(i)

    # find root of an indexment 
    def root(self,index):
        while self.arr[index] != index:
            index = self.Arr[index]
        return index

    # set root of an index to its grandparent 
    def root_path_compressed(self,index):

        while self.arr[index] != index:
            self.arr[index] = self.arr[self.arr[index]]
            index = self.arr[index]
        return index

    # union of two by updating the root
    def wt_union(self,A,B):
        root_a = self.root(A)
        root_b = self.root(B)

        if self.size[root_a] < self.size[root_b]:
            self.arr[root_a] = root_b
            self.size[root_b] += self.size[root_a]
        else:
            self.arr[root_b] = root_a
            self.size[root_a] += self.size[root_b]

    # find: if two indexments have same root,they are connected
    def find(self,A,B):

        if self.root(A) == self.root(B):
            return True
        return False

