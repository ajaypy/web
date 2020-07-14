"""
given an array of numbers
find set of 3 whose sum is 0

handle dumplicates in the given array by checking and incrementing
"""


#solution 1: using sliding window
#sort the array. As the sliding window is N**2 sorting won't add to complexity

class 3sum_sliding_window:
    def 3sum_two_pointer(self,nums):
        res = []
        nums.sort()
    
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.2sums(nums,i,res)
    
        return res
    
    def 2sums(self,nums,i,res):
        lo, hi= i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0 or (lo > i + 1 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif sum > 0 or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1

#solution 2: using Hashset
# handling duplicates in hashset is not as easy as in case of using sliding windows    
