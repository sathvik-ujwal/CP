'''
You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

For each queries[i]:

Select a subset of indices within the range [li, ri] in nums.
Decrement the values at the selected indices by 1.
A Zero Array is an array where all elements are equal to 0.

Return true if it is possible to transform nums into a Zero Array after processing 
all the queries sequentially, otherwise return false.
'''

#3355 leetcode
# instead of subtracting 1 from each element in the range, we can subtract 
# 1 from the l the element and add 1 to the r+1 th element 
# when we do the prefix sum of this array we get the required array
# example
# say we have an array 5 5 5 5 5
# we have l and r as 0 and 3
# subtracting 1 from l to r gives us 4 4 4 4 5
# instead what can take an array of zeros 0 0 0 0 0
# add 1 to the lth element and subtract 1 from r+1 th element
# then we go from iterate through nums while adding calculating the prefix sum
# if the prefix sum is less than the element at that index then we return False

# O(n + m) where n is len of nums and m is len of queries

from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n  = len(nums)
        d = [0]*n
        for l, r in queries:
            d[l] += 1
            if r + 1 < len(nums):
                d[r+1] -= 1

        curr = 0
        for i in range(n):
            curr += d[i]

            if curr < nums[i]:
                return False
        return True
             