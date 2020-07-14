"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.


#1. replace multiple repeated '*' with '*'
#2. Set the rules: 
#3. pointers/indexes: p_s : pointer to current character in s
              p_p : pointer to current character in p

    1. if  P[p_p] 'q'
           go next
    2. if  P[p_p:] is '*' return Matched
    3. if  P[p_p] is '*' and P[p_p + 1] == S[p_s]  == match
    4. if  P[p_p] is '*' and P[p_p + 1] in S[p_s+1:] == match

    No match
    https://leetcode.com/articles/wildcard-matching/
"""


def remove_repeated_starts(P):

    if len(P) == 0:
        return P
    p1 = [P[0],]
    for x in P[1:]:
        if p1[-1] != '*' or p1[-1] == '*' and x != '*':
            p1.append(x)

    return ''.join(p1)



def wildcard_match(S,P):

    LS = len(S)
    LP = len(P)

    if LS == 0 or LP == 0:
        return True

    p_s = p_p = 0

    match = False
    while p_s < LS and p_p < LP:

        print ('P_P: ',p_p, '  P_S: ', p_s)
        if P == '*':
            match = True
            break 
        elif P[p_p] == '?' or P[p_p] == S[p_s]:
            p_p += 1
            p_s += 1
        elif P[p_p] == '*':
            if p_p == LP - 1:
                match = True
                break
            else:
                x = p_s
                print ('P_P: ',p_p, '  P_S: ', p_s, 'X :',x)
                while x < LS and S[x] == P[p_p + 1]:
                    x += 1
                    print ('P_P: ',p_p, '  P_S: ', p_s, 'X :',x)
                print ('RRR P_P: ',p_p, '  P_S: ', p_s, 'X :',x)
                if x == LS:
                    break
                else:
                    print ('P_P: ',p_p, '  P_S: ', p_s)
                    p_s = x + 1
                    p_p += 2
                    if p_p >= LP and p_s >= LS:
                        match = True
    print (match)
    return match


P = '*ab**c******d*'
p1 =  remove_repeated_starts(P)
print (p1)

S = 'aa'
P = 'a'
P = '*a'
match = wildcard_match(S,P)
print (match)
