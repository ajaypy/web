import pdb
class LRU_Cache:

    def __init__(self, original_function, maxsize=1024):
        # Link structure: [PREV, NEXT, KEY, VALUE]
        self.root = [None, None, None, None]
        self.root[0] = self.root[1] = self.root
        self.original_function = original_function
        self.maxsize = maxsize
        self.mapping = {}

    def __call__(self, *key):
        mapping = self.mapping
        root = self.root
        link = mapping.get(key)
        print (link)
        if link is not None:
            link_prev, link_next, link_key, value = link
            a,b,c,d = link
            pdb.set_trace()
            print (link_prev[0][0])
            link_prev[1] = link_next
            link_next[0] = link_prev
            last = root[0]
            last[1] = root[0] = link
            link[0] = last
            link[1] = root
            return value
        value = self.original_function(*key)
        if len(mapping) >= self.maxsize:
            oldest = root[1]
            next_oldest = oldest[1]
            root[1] = next_oldest
            next_oldest[0] = root
            del mapping[oldest[2]]
        last = root[0]
        last[1] = root[0] = mapping[key] = [last, root, key, value]
        return value


if __name__ == '__main__':
    p = LRU_Cache(ord, maxsize=9)
    for c in 'aa':
        print(c, p(c))

