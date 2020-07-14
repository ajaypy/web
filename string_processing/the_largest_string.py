"""
Given a string, construct a new string by rearranging the original string and deleting characters as per your need.
Return the lexographically largest string that can be constructed where there is a limit as to how many consecutive characters can be the same.


Example:
A new string cannot have more than k=2 consecutive chanraters that are same.  
s = "baccc"
Output can be "ccbca" but not "cccba"

def getLargestString (str1,k):
    return 'Longest lexicographically arranged string"

Constraints:
    1 <= n <= 10**5
    1 <= k <= 10**3
    only a-z

"""

"""
#1. count the instances of all the characters
#2. recreate the new string by inserting the ones with the highest frequency first
Optimizations:
#3. if length < k, return as such
#4. if lenght > k, and all characters are same, return k-1
"""

def get_longest_consecutive(S, k):

    ma_d = {}
    i = 1
    cur = S[0]
    while i <= (len(S) - 1):
        print ("I=%r , L= %r, S[i]= %r, cur= %r" % (i,L,S[i],cur))

        if S[i] != cur:
            if i - L >= k :
               ma_d.setdefault(cur, [])
               ma_d[cur].append([L,i-1])
            L = i
            cur = S[i]
        elif (i == len(S) - 1):
                if i - L - 1 >= k :
                   ma_d.setdefault(cur, [])
                   ma_d[cur].append([L,i])
        
        i += 1
            
    return ma_d


def get_largest_string(S, k):
    ch_d = {}
    for char in "abcdefghijklmnopqrstuvwxyz":
        ch_d[char] = 0

    for char in S:
        ch_d[char] += 1 

    retstr = ""

    while 1: 
        chars_with_k = 0
        for key, v in ch_d.items():
            if v <= 0:
                continue
            elif v >= k:
                got_largest = False
                retstr += key*(k-1)
                ch_d[key] -= (k-1)
            else:
                retstr += key
                ch_d[key] -= 1

    return retstr
S =  "bacccddfdddddxddddddde"
k = 3
print (get_largest_string(S,k))
print (S, len(S))
