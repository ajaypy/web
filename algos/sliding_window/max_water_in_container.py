"""
find the maximum water that can be collected between  multiple 
walls of varying heights


find the max area
start with max width and then keep optmizing by varying the heights
"""

def max_water(vert):

    if len(vert) == 0:
        return 0

    lp = 0
    rp = len(vert) - 1

    max_water = 0
    while rp - lp >= 1:
        max_water = max(max_water,min(vert[rp], vert[lp]) * (rp -lp))
        if vert[lp] < vert[rp]:
            lp += 1
        else:
            rp -= 1
        print (lp,rp, max_water)

    print (lp,rp, max_water)


vert = [11,8,6,2,5,4,8,3,7]
max_water(vert)
