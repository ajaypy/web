"""
Given an array of non-negative integers, you are initially positioned at the 
first index of the array.
Each element in the array represents your maximum jump length at that position.
"""


class jumps_to_end:
    def __init__(self, nums):
        self.nums = nums
        self.jumps = [False]* len(nums)
        self.jumps[-1] = True
        self.m_i = len(self.nums) - 1

    def can_jump(self):

        nums = self.nums
        m_i = self.m_i

        for i in range(self.m_i ,-1,-1):
            if self.jumps[i]:
                continue

            if self.nums[i] == 0:
                continue

            if (i + nums[i] >= (m_i)):
                self.jumps[i] = True

            if (True in self.jumps[i+1 : min (i + nums[i] + 1, m_i+1)]):
                self.jumps[i] = True

arr = [3,2,1,0,4]
arr = [2,3,1,1,4]
jte = jumps_to_end(arr)
jte.can_jump()
print (jte.jumps)
