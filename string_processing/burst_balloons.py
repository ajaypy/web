"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.


Problem:
    Maximize with divisions
    Divisions of 3

    Once you remove, how to store the rest? space complexity and multiple loops
    space can be solved by solved by marking with special character

    but loops 

    and how to prove this is maximum

    maximum is sum of max local sums

https://leetcode.com/articles/burst-balloons/
"""

def burst_balloons(nums):

    burst_index = []

    N = len(nums)
    i = 0
    while True:
        if i < N - 2:
            if nums[i] > nums[i+1] and nums[i+1] < nums[i+2]:
                burst_index.append(i+1)
                i += 2
            else:
                i += 1
        else:
            break
    print (burst_index)

nums = [3,1,5,8]
nums = [3,1,5,6,8,7,9,10]
nums = [3,5,6,8,9,10]
burst_balloons(nums)


