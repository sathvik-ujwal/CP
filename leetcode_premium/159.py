#Longest Substring with At Most Two Distinct Characters

'''
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
'''
from collections import defaultdict

class Solution:
    def longest_substring(self, s: str) -> int:
        res = 0 
        d = defaultdict(int)
        left = 0

        for right, c in enumerate(s):
            d[c] += 1

            while len(d) > 2:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left += 1

            res = max(res, right-left+1)

        return res 

sol = Solution()
s = "ccaabbb"
result = sol.longest_substring(s)
print(result) 