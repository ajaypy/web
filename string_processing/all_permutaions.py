"""
given a string get all permutations

for 'abc' the answer is ['abc', 'acb','bca','bac','cab','cba']
"""


def get_permutes_iterative(S):

    L = len(S)
    ans = []

    for i in range(L):
        for j in range(L):
            if i == j:
                continue
            elif j > i:
                ans.append( S[i] + S[j:] + S[:i] + S[i+1:j])
            else:
                ans.append(S[i] + S[j:i] + S[i+1:] + S[:j])
    return (ans)

S = 'abcdef'
all_permutes = get_permutes_iterative(S)
print (all_permutes)
