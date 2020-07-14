"""
LRU Cache
Limit size, evicting the least recently looked-up key when full

Data structure:
#1. random access , update, removal
#2. max size (max number of key, value pairs
#3. size of the indivial key and value

Linked list doesn't have random access
Hasmap has issues in managing insertion/update times


use a double linked list with a hash map. Linked list to keep track of last and earliest accessed
"""

from collections import OrderedDict

#1. LRU using the OrderedDict
class LRU(OrderedDict):

    def __init__(self, maxsize=128, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]
lru1 = LRU()
i = 10
for x in "abcdefgh":
    lru1[x] = i
    i += 1

print (lru1)
lru1['c'] = 99
print (lru1)

