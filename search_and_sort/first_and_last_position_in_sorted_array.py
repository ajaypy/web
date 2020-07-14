"""
Given a sorted array, find the left and right most occurences of a target

binary search : 3 cases at every step

1. mid < target
2. mid > target
3. mid == target

case 1 and 2: give indication where L and R will reside and we continue
case 3: mid can be L or mid can be R
        so it we looking for Left index, make hi = mid and finally lo will
        sync

        if we looking for right index,make lo = mid+1 and finally lo will 
        sync


        As we are returning lo,so need to bring lo the position
"""

def get_left_index(nums, target,left):

    lo = 0
    hi = len(nums)

    while lo < hi:
        mid = lo + (hi - lo)//2
        if (nums[mid] > target) or (left and target == nums[mid]):
            hi = mid['(', '(', '(', '(']

