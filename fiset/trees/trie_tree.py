"""
implement a trie
https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
"""
from collections import defaultdict
class trie_node():

    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class trie():
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return trie_node()

    def get_index(self,ch):
        return ord(ch) - ord('a')

    def insert(self,word):
        root = self.root
        len1 = len(word)

        for ch in word:

            if ch not in root.children:
                root.children[ch] = self.get_node()
            root = root.children[ch]
        root.terminating = True

    def search(self,word):
        root = self.root
        len1 = len(word)

        for ch in word:
            if not root:
                return False
            root = root.children.get(ch)

        return True if root and root.terminating else False

    def delete(self,word):
        root = self.root

        for ch in word:
            if not root:
                print ("Word not found")
                return -1
            root = root.children.get(ch)
        if not root:
            print ("Word not found")
            return -1
        else:
            root.terminating = False
            return 0
    def update(self,old_word, new_word):
        val = self.delete(old_word)
        if val == 0:
            self.insert(new_word)

if __name__ == "__main__":
    strings = ["pqrs", "pprt", "psst", "qqrs", "pqrs"]

    t = trie()
    for word in strings:
        t.insert(word)

    for word in strings:
        print (t.search(word))
        print (t.search(word + 'xyz'))

    t.delete("pprt")
    print (t.search("pprt"))

    t.update("pprt","abcd")
    print ("kkkkk ------------- kkkkkkk")
    print (t.search("pprtabcd"))
    print (t.root.children)
    tmp = t.root.children['p'].children
    print (tmp)
    print (tmp['p'].children)
    print (t.search("abcd"))




