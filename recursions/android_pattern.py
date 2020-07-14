"""
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

 

Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.

https://leetcode.com/articles/android-unlock-patterns/

Recursion + Backtracking
Recursion : Cotinue forward till it works
Backtracking: Restart recusion when the current fails


Need to find all patterns for each length
so the same search has to be run over (n-m) times

"""

class Solution:
    used = [False] * 9

    def num_of_patterns(m,n):
        res = 0
        for len in range(m,n+1):
            res += calc_patterns(-1, len)
            for i in range(9):
                used[i] = False
        return res

    def is_valid(index,last):

        if used[index]:
            return False

        if last == -1:
            return True

        
