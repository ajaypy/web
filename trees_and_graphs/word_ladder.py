"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.


Its a unweighted, undirected graph
nodes are words
edges are changed characters , leading to transformation from one word 
to another


Graph : BFS Breadth First Search
https://leetcode.com/articles/word-ladder/
"""
from collections import defaultdict
from collections import deque
def ladder_length(b_word, e_word, word_list):

    L = len(b_word)

    # combo_dict to store all words that can be formed by changing one character
    # in each word

    combo_dict = defaultdict(list)
    for word in word_list:
        for i in range(L):
            combo_dict[word[:i] + "*" + word[i+1:]].append(word)

    for item in combo_dict.items():
        print (item)


    #queue for BFS
    #queue has  nodes and their level / distance from b_word
    queue = deque([(b_word,1)])
    visited = {b_word: True}

    while queue:
        c_word, level = queue.popleft()
        for i in range(L):
            i_word = c_word[:i] + "*" + c_word[i+1:]

            for word in combo_dict[i_word]:
                if word == e_word:
                    return level + 1

                if word not in visited:
                    visited[word] = True
                    queue.append((word, level+1))
            combo_dict[i_word] = []
    return 0


  

word_list = ["hot","dot","dog","lot","log","cog"]
dist = ladder_length("hit", "cog", word_list)
print (dist)
