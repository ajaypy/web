"""
get all substrings of a string
"""

def all_substrings(S):
    L = len(S)
    ans = []

    for i in range(L):
        for  j in range(i+1,L):
            ans.append(S[i:j])

    return ans

S = "abcdef"
subs = all_substrings(S)
print (subs)
