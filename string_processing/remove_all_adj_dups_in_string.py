"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the 
answer is unique.
"""

# recurise solution
"""
traverse: if no dup return
if dup: find all the dups, make the recursive call
"""

def remove_adjacent_dups_recursion(S):

    print (S)
    N = len(S)
    left = -1 
    i = 1
    while i < N:
        if S[i] == S[i-1]:
            left = i
            while (S[i] == S[i-1]) and i < N:
                i += 1
            break
        i += 1
    if left != -1:
        print ("LEFT:",left)
        new_S = S[:left-1] + S[i:]
        return  remove_adjacent_dups_recursion(new_S)
    return S

s1 = "abbacaaad"
nd =  remove_adjacent_dups_recursion(s1)
print (nd)



def remove_adjacent_dups_stack(S):

    print (S)
    N = len(S)
    stack = []
    for i in range(N):
        if stack and S[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(S[i])
        print (i, S[i], stack)
    return ''.join(stack)

s1 = "abbacaaaad"
nd =  remove_adjacent_dups_stack(s1)
print (nd)
