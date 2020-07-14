"""
Given a string, find the longest substring with no characters repeated
"""

def no_repeat_char_substring(S):

    L = len(S)
    if L <= 1:
        return S

    ans = S[0]
    lo = 0
    hi = 1

    while hi < L:
        if S[hi] in S[lo:hi]:
            if (hi - lo ) > len(ans):
                ans = S[lo:hi]
            lo = hi
        hi += 1

    return ans

S = "abcabcbb"
ans = no_repeat_char_substring(S)
print (ans)
