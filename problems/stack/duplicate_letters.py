'''
Remove duplicate Letters (316)

Given a string s, remove duplicate letters so that every letter appears once and 
only once. You must make sure your result is the smallest in lexicographical order
among all possible results

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c:i for i,c in enumerate(s)}
        stack = []
        for i,c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)       