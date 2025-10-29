#One Edit Distance

'''
Given two strings s and t, determine if they are both one edit distance apart.
'''
from functools import lru_cache
class Solution:
    def edit_distance(self, s: str, t: str) -> bool:
        sl, tl = len(s), len(t)

        if abs(sl-tl) > 1:
            return False

        @lru_cache(None)
        def recursion(i, j, used):
            if (i >= sl and j >= tl):
                return True
            if (i >= sl or j >= tl):
                return not used

            if s[i] == t[j]:
                return recursion(i+1, j+1, used)
            else:
                if used:
                    return False
                return recursion(i, j+1, True) or recursion(i+1,j+1, True) or recursion(i+1, j, True)

        
        return recursion(0, 0, False)


sol = Solution()
print("Enter s")
s = input()
print("Enter t")
t = input()
res = sol.edit_distance(s, t)
print(res)