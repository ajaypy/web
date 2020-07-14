"""
basic implementation of PQ with a heap
https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/tutorial/
"""

class Node:
    def __init__(self,priority):
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.queue = list()


    def size(self):
        return len(self.queue)

    # simple insertion. insert before the first existing node with higher priority
    def insert(self,node):
        if self.size() == 0:
            self.queue.append(node)
        else:
            for x in range(self.size()):
                if node.priority >= self.queue[x].priority:
                    if x == self.size() - 1:
                        self.queue.insert(x+1,node)
                    else:
                        continue
                else:
                    self.queue.insert(x,node)
                    return True

    def delete(self):
        return self.queue.pop(0)

    def show(self):
        for x in self.queue:
            print (str(x.priority))

pq = PriorityQueue()
for i in [100,1,3,11,2,5,32]:
    pq.insert(Node(i))
pq.show()
print (pq.delete())
pq.show()
