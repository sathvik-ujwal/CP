# partition labels 
'''
You are given a string s consisting of lowercase english letters.
We want to split the string into as many substrings as possible,
while ensuring that each letter appears in at most one substring.
Return a list of integers representing the size of these substrings 
in the order they appear in the string.

example:
Input: s = "xyxxyzbzbbisl"
Output: [5, 5, 1, 1, 1]
'''

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurance = {}
        for i, c in enumerate(s):
            last_occurance[c] = i

        res = []
        start, end = 0, 0
        for i, c in enumerate(s):
            start += 1
            end = max(end, last_occurance[c])

            if i == end:
                res.append(start)
                start = 0
        return res