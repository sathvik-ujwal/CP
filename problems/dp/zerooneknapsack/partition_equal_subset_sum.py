# partition equal subset sum
# leetcode 416
'''
given an array return true if you can partition them into two equal subsets
'''

# 0/1 knapsack
# take half of the sum of nums . ie target
# choose elements from the nums to acheive target 

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        s = s//2
        dp = {}
        
        def recursion(nums, s, s2, n):
            if n == 0 and s == s2:
                return True
            elif n == 0:
                return False
            
            if (s2, n) in dp:
                return dp[(s2, n)]
            
            
            dp[(s2, n)] =  recursion(nums, s, s2 + nums[n-1], n-1) or recursion(nums, s, s2, n-1)     
            return dp[(s2,n)]
        return recursion(nums, s, 0, len(nums))

            
           