# 873 longest fibonacci subsequence

'''
A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, 
return the length of the longest Fibonacci-like subsequence of arr. If one does 
not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements
(including none) from arr, without changing the order of the remaining elements. For example,
[3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
'''

# brute force

def longestFibonacciSubsequence(nums):
    numset = set(nums)
    res = 0
    n = len(nums)
    
    for start in range(n-2):
        for next in range(start+1, n-1):
            prev = nums[start]
            curr = nums[start] + nums[next]
            curr_len = 2
            
            while curr in numset:
                prev, curr = curr, curr+ prev
                curr_len += 1
            res = max(res, curr_len)
            
    return res if res > 2 else 0
                
            
        
    