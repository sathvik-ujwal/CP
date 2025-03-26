# partition into k subsets
'''
return True if array can be divided into k equal subsets
'''

from typing import List

# recursive solution (TLE)

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
          
        if sum(nums) % k  != 0:
            return False

        if len(nums) < k:
            return False
        
        target = s/k
        nums.sort(reverse=True)
        visited = [False] * len(nums)

        def recursion(remaining, curr_sum=0, next_index=0):
            if remaining == 1:
                return True

            if curr_sum == target:
                return recursion(remaining - 1)

            for i in range(next_index, len(nums)):
                if curr_sum + nums[i] <= target and visited[i] == False:
                    visited[i] = True

                    if recursion(remaining, curr_sum=curr_sum+nums[i], next_index=i+1):
                        return True
                    visited[i] = False
            return False
        return recursion(k)
                


  
    
    