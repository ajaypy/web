class BinaryTree:

    def __init__(self, nodes = []):
        self.nodes = nodes


    def root(self):
        return self.nodes[0]

    def iparent(self,i):
        return (i-1)//2

    def ileft(self,i):
        return 2*1 + 1

    def iright(self,i):
        return 2*1 + 2

    def left(self,i):
        return self.node_at_index(self.ileft(i))

    def right(self,i):
        return self.node_at_index(self.iright(i))

    def parent(self,i):
        return self.node_at_index(self.iparent(i))

    def node_at_index(self,i):
        return self.nodes[i]

    def size(self,i):
        return len(self.nodes)

class MinHeap(BinaryTree):

    def __init__(self,node):
        BinaryTree.__init__(self,nodes)
        self.min_heapify()


    # find the index which is minimum among i, ileft, iright
    # parent needs to be less than left and right childs
    # find the min between the parent and the two childs and swap them
    def min_heapify_subtree(self,i):
        size = self.size()
        ileft = self.ileft(i)
        iright = self.iright(i)

        imin = i
        if (ileft < size and self.nodes[ileft] < self.nodes[imin]):
            imin = ileft
        if (iright < size and self.nodes[iright] < self.nodes[imin]):
            imin = iright

        if (imin != i):
            self.nodes[i],self.nodes[imin] = self.nodes[imin],self.nodes[i]
            self.min_heapify_subtree(imin)

    def min_heapify(self):
        for i in range(len(self.nodes), -1, -1):
            self.min_heapify_subtree(i)

    def min(self):
        return self.nodes[0]

    def pop(self):
        min_node = self.nodes[0]

        if self.size() > 1:
            self.nodes[0] = self.nodes[-1]
            self.nodes.pop()
            self.min_heapify_subtree(0)
        elif self.size() == 1:
            self.nodes.pop()
        else:
            return None

        return min_node
