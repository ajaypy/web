"""
Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it is able to trap after raining.

The water at any index is 
height * width
height = min of (highest to left and highest to right) - (self height)

https://www.geeksforgeeks.org/trapping-rain-water/
"""

# Sol1 : Brute force
"""

#1. Initialize ans=0ans=0
#2. Iterate the array from left to right:
#3. Initialize \text{left\_max}=0left_max=0 and \text{right\_max}=0right_max=0
#4. Iterate from the current element to the beginning of array updating:
{left_max}=max({left_max},{height}[j])left_max=max(left_max,height[j])
#5. Iterate from the current element to the end of array updating:
\text{right\_max}=\max(\text{right\_max},\text{height}[j])right_max=max(right_max,height[j])
#6. Add \min(\text{left\_max},\text{right\_max}) - \text{height}[i]min(left_max,right_max)−height[i] to \text{ans}ans
width = 1
"""
def get_rain_water(hts):

    ans = 0

    lh = len(hts)

    for i in range(0,lh):
        left = hts[i]
        for j in range(i):
            left = max(left,hts[j])

        right = hts[i]
        for j in range(i+1,lh):
            right = max(right,hts[j])

        ans = ans + (min(left,right) - hts[i])

    return ans

hts = [0,1,0,2,1,0,1,3,2,1,2,1]
print (get_rain_water(hts))



# Sol2: Dynamic Programming
"""
In brute force, we iterate over the left and right
#. Find min height of bar from the left end upto an index i L_MAX
#. Find max height of bar from the right end upto an index i L_MAX
#. Iterate over the height array and update ans
Time:
    O(N)
Space:
    O(N) : actual = 2N
"""

def get_rain_water_dyn(hts):

    if len(hts) == 0:
        return 0

    ans = 0
    lh = len(hts)

    left = [0] * lh
    right = [0] * lh

    left[0] = hts[0]
    right[lh-1] = hts[lh-1]
    for i in range(1,lh):
            left [i]= max(left[i-1],hts[i])
    for i in range(lh-2,-1,-1):
            right [i]= max(right[i+1],hts[i])


    for i in range(lh):
        ans = ans + (min(left[i],right[i]) - hts[i])


    return ans


print (get_rain_water_dyn(hts))


# Sol3: Sliding Window + Dynamic
"""
A contracting sliding window
need the minimum of the high from left and right

Dynamic: known solutions exist at the end
For the left index, the max_left is known
For the right index, the max_right is known
Start from the known and use that to get the unknowns
"""

def get_rain_water_opt_dyn(hts):

    if len(hts) == 0:
        return 0

    ans = 0
    lh = len(hts)

    l_max = 0
    r_max = 0

    lo = 0
    hi = lh - 1

    while (lo <= hi):
        if (hts[lo] <= hts[hi]):
            if hts[lo] > l_max:
                l_max = hts[lo]
            else:
                ans += l_max - hts[lo]
            lo += 1
        else:
            if hts[hi] > r_max:
                r_max = hts[hi]
            else:
                ans += r_max - hts[hi]
            hi -= 1

    return ans
       
print (get_rain_water_opt_dyn(hts))

