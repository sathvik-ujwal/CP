# target sum leetcode 494

from collections import defaultdict
from typing import List

# recursion (TLE) 
# Time complexity O(2^n)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def recursion(nums, target, n):
            if n == 0 and target == 0:
                return 1
            elif n == 0:
                return 0
            
            return recursion(nums, target-nums[n-1], n-1) + recursion(nums, target+nums[n-1], n-1)

        return recursion(nums , target, len(nums))
        

# Memoizatoin 
# Time complexity O(n^2)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        dp = [[-1]*(s*2+1) for _ in range(len(nums)+1)]
        def recursion(nums, target, n, res):
            if n == 0 and res == target:
                return 1
            elif n == 0:
                return 0
            
            if dp[n][s + res] != -1:
                return dp[n][s + res]
            
            dp[n][s+res] = recursion(nums, target, n-1, res-nums[n-1]) + recursion(nums, target, n-1, res +nums[n-1])

            return dp[n][res + s]
        recursion(nums, target, len(nums),0)
        print(dp)
        return dp[-1][s]
        

# top down approach 
# the memoization can also be done using a defaultdict to simply it 

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums)+1)]
        dp[0][0] = 1 

        for i in range(len(nums)):
            for curr_sum , count in dp[i].items():
                dp[i+1][curr_sum + nums[i]] += count
                dp[i+1][curr_sum - nums[i]] += count

        return dp[len(nums)][target]

            