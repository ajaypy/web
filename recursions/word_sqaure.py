"""
find word ball from a list of words
https://leetcode.com/articles/word-squares/
"""
"""
class Solution:

    def wordSquares(self, words: List[str]) -> List[List[str]]:

        self.words = words
        self.N = len(words[0])

        results = []
        word_squares = []
        for word in words:
            # try with every word as the starting word
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def backtracking(self, step, word_squares, results):

        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])
        # find out all words that start with the given prefix
        for candidate in self.getWordsWithPrefix(prefix):
            # iterate row by row
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()

    def getWordsWithPrefix(self, prefix):
        for word in self.words:
            if word.startswith(prefix):
                yield word


class Solution_Trie:

    def word_squares(self, words):

        self.words = words
        self.N = len(words[0])
        self.build_trie(self.words)

        results = []
        word_squares = []
        for word in words:
            word_squares = [word]
            self.bt(1,word_squares,results)
        return results

    def build_trie(self,words):
        self.trie = {}

        for word_index,word in enumerate(words):
            node = self.trie

            for char in word:
                if char in node:
                    node = node[char]
                else:
                    new_node = {}
                    new_node["#"] = []
                    node[char] = new_node
                node["#"].append(word_index)


"""
def build_trie(words):
        trie = {}

        for word_index,word in enumerate(words):
            node = trie

            for char in word:
                if char in node:
                    node = node[char]
                else:
                    new_node = {}
                    new_node["#"] = []
                    node[char] = new_node
                    node = new_node
                node["#"].append(word_index)

        for item in trie.items():
            print (item)
        for item in trie.keys():
            print (item)
        for item in trie.values():
            print (item)


words = ['ball', 'lead','area','able','lady']
build_trie(words)


