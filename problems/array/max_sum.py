# 1749 Maximum sum of subarray

'''
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
'''

def maxAbsSum(nums):
    prefix = [0] * (len(nums)+1)
    for i in range(len(nums)):
        prefix[i+1] = prefix[i] + nums[i]
    return abs(max(prefix) - min(prefix))    