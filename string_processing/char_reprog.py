"""
Find the max number of moves that can be removed to reach the same final 
destinaton
"""

def get_max_deletions(S):

    U = 1
    D = -1
    R = 1
    L = -1

    pos = [0,0]
    
    for c in S:
        if c == "U":
           pos[1] += U
        elif c == "D":
           pos[1] += D
        elif c == "R":
           pos[0] += R
        elif c == "L":
           pos[0] += L
        else:
           print ("Unknown Character")
    return pos

for S in ["URDRLL", "DLLLLLLLLLLLDLLLLLLLLLRLLLLLLUU"] :
    fP =  get_max_deletions(S)
    print (fP)
    print (S, "  : ", len(S) - (abs(fP[0]) + abs(fP[1])))
