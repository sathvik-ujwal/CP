# Group Shifted Strings

'''
Given a string, we can "shift" each of its letter to its successive letter, for example:
"abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings
that belong to the same shifting sequence.
'''

class Solution:
    def shifted_strings(self, arr: list[str]) -> list[list[str]]:
        d = {}
        start = ord('a')

        for string in arr:
            prev = None
            tup = []
            for c in string:
                if prev == None:
                    prev = ord(c)-start 
                else:
                    curr = ord(c)-start 
                    tup.append(min(abs(prev-curr), 26-prev+curr, 26-curr+prev))
            adder = tuple(tup)
            if adder not in d:
                d[adder] = [string]
            else:
                d[adder].append(string)
        return [val for key, val in d.items()]


sol = Solution()
arr = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
res = sol.shifted_strings(arr)
print(res)
                



