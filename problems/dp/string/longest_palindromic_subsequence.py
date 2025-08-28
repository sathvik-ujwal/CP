'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
'''



class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        mem = {}
        
        def recursion(i, j):
            if i == j:
                return 1
            if i > j:
                return 0

            if (i,j) in mem:
                return mem[(i,j)]

            if s[i] == s[j]:
                res = 2 + recursion(i+1, j-1)
            else:
                res = max(recursion(i+1, j), recursion(i, j-1))

            mem[(i,j)] =res
            return res

        
        return recursion(0, len(s)-1)