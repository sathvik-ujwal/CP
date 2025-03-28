# longest common subsequence 1143
'''
Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some
characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1]*(len(text1)+1) for _ in range(len(text2)+1)]

        def recursion(t1, t2, n1, n2):
            if n1 == 0 or n2 == 0:
                return 0
            
            if dp[n2][n1] != -1:
                return dp[n2][n1]

            if t1[n1-1] == t2[n2-1]:
                dp[n2][n1] = 1 + recursion(t1, t2, n1-1, n2-1)
            else:
                dp[n2][n1] = max(recursion(t1 ,t2, n1-1, n2), recursion(t1,t2, n1, n2-1))
            return dp[n2][n1]

        return recursion(text1, text2, len(text1), len(text2))

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1]*(len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(len(text2)+1):
            dp[0][i] = 0

        for i in range(len(text1)+1):
            dp[i][0] = 0

        for i in range(1,len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]

        
