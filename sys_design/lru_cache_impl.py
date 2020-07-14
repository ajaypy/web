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

#1. LRU using two hash maps
class LRUCache:

    def __init__(self, maxsize=128):
        self.maxsize = maxsize
        self.tm = 0
        self.cache = {}
        self.lru = {}

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        return -1

    def set(self, key, value):
        if len(self.cache) >= self.maxsize:
            old_key = min(self.lru.keys(), key = lambda k:self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key] = self.tm
        self.tm += 1
lruc = LRUCache(3)
lruc.set('a',4)
lruc.set('a',4)
lruc.set('a',5)
lruc.set('a',4)
lruc.set('b',4)
lruc.set('c',4)
lruc.set('d',4)

print(lruc.lru)


# Implement using OrderedDict
# to update the time stamp, do a pop and set for GET
# to update the time stamp check for size, do a pop and set for SETkkkkkkkkkkkkkkkkkkkkkkkkkkkk`:w


import collections

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value
