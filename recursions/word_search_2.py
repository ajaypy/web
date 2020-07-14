"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word

https://leetcode.com/articles/word-search-ii/
"""


# Sol1: Backtracking with Trie
"""
create a Trie
Traverse the matrix and match in the Trie
"""

class Solution:

    def find_words(board, words):

        WORD_KEY = "$"

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter,{})
            node[WORD_KEY] = word

        for k in trie:
            print (k, trie[k])

        row_num = len(board)
        col_num = len(board[0])

        matched_words = []

    def back_tracking(row, col, parent):

        letter = board[row][col]
        cur_node = parent[letter]

        word_match = cur_node.pop(WORD_KEY,False)
        if word_match:
            matched_words.append(word_match)

        board[row][col] = "#"
        for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            newRow, newCol = row + rowOffset, col + colOffset     
            if newRow < 0 or newRow >= row_num or newCol < 0 or newCol >= col_num:
                continue
            if not board[newRow][newCol] in curr_node:
                continue
            back_tracking(newRow, newCol, curr_node)
        board[row][col] = "letter"


        if not curr_node:
            parent.pop(letter)





words = ['oath','dig','dog','dogs']
find_words([],words)

