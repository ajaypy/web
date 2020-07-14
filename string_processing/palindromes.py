"""
longest palindrome 
"""


def longest_palindrome_with_DP(S):

    N = len(S)
    R = [[ 0 for x in range(N)] for x in range(N)]

    for i in range(N):
        R[i][i] = 1

    # line with length 1 is always palindrome
    # iterate over palindrome lengths from 2 to len(S), usin these palindromes
    # if a charater is palindrome, and left right to it are same, its a palindrome
    # i: first character of substring we are currently testing
    # j: last character of substring we are currently testing

    for cl in range(2,N+1):
        for i in range(N-cl + 1):
            j = i + cl - 1
            if S[i] == S[j] and cl == 2:
                R[i][j] = 2
            elif S[i] == S[j]:
                R[i][j] = R[i+1][j-1] + 2
            else:
                R[i][j] = max(R[i][j-1],R[i+1][j])

    for row in R:
        print (row)
    return R[0][N-1]




S = "abeeba"
pal = longest_palindrome_with_DP(S)
print (pal)

def longest_palindrome_expand_around_center(S):

    L = len(S)
    if L <= 1:
        return S

    start = end = 0

    for i in range(L):
        len1 = expandAroundCenter(S,i,i)
        len2 = expandAroundCenter(S,i,i+1)
        max_len = max(len1, len2)

        if (max_len >  end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            print (start,  end)
    return S[start:end+1]

def expandAroundCenter(S,left,right):
    L = left
    R = right

    while (L >= 0 and R < len(S) and S[L] == S[R]):
        L -= 1
        R += 1
    return R - L - 1

pln = longest_palindrome_expand_around_center(S)
print (pln)
