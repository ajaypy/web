"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n
"""

def get_st_numbers(N):

    sn = {}
    if N == 0:
        return [""]
    elif N == 1:
        return ["0","1","8"]
    elif N == 2:
        return ["11","88","69","96"]
    

    outer = get_st_numbers(2)
    print (outer)
    middle = get_st_numbers(N -2)

    sn[N] = []
    #if N % 2 == 0:
    #    middle.append("0"*(N-2))
    middle.append("0"*(N-2))
    for ele in outer:
        for mid in middle:
            sn[N].append(ele[0] + mid + ele[1])
    print (sn[N])
    return sn[N]
#get_st_numbers(3)
#get_st_numbers(4)
get_st_numbers(5)
#get_st_numbers(6)
