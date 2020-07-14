"""
To some string S, we will perform some replacement operations that replace groups of letters with new ones (not necessarily the same size).

Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.  The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y.  If not, we do nothing.

Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
Output: "eeebffff"
Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
"cd" starts at index 2 in S, so it's replaced by "ffff".

Input: S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation: "ab" starts at index 0 in S, so it's replaced by "eee".
"ec" doesn't starts at index 2 in the original S, so we do nothing.

"""


def find_and_replace(S,indexes,src,t):
    found = False
    for i in range(len(indexes)):
        start = indexes[i]
        print( start, ":",len(src[i]))
        print( S[start:i+len(src[i])])
        print( src[i])
        if S[start: start+ len(src[i])] != src[i]:
            break
        found = True

    if found:
        ans = ''
        i = 0
        while i < (len(S)):
            for j in range(len(indexes)):
                append_end = indexes[j] 
                ans += S[i:append_end]
                ans += t[j]
                i+= len(src[j])+1
            ans += S[i:]
            print (ans)

S = "abcd"
indexes = [0,2]
src = ["a", "cd"]
t = ["eee", "ffff"]
find_and_replace(S,indexes,src,t)
