"""
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

# Binary Search + Rabin-Karp
https://leetcode.com/articles/longest-repeating-substring/
"""

# my solution
"""
find the indexes of each character
then check starting from the characters which are more than one

find substring 
check if they are duplicate
"""

def longest_repeated_substring(S):
    n = len(S)

    left, right = 1,n
    while left <= right:
        L = left + (right - left) // 2
        if search_substr(L,n,S) != -1:
            left = L + 1
        else:
            right = L - 1

    return left - 1


