# leetcode 76
'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
'''

# function to check if the substring has all the character in the other substring
# used for brute force approach where you check all substrings 
def isValid(s, p):
    char = [0]*256
    
    for c in p:
        char[ord(c)] += 1
    
    for c in s:
        if char[ord(c)] > 0:
            char[ord(c)] -= 1
    
    return all(c == 0 for c in char)

class Solution:
    def minWindow(self, s, p):
        slen = len(s)
        plen = len(p)
        
        if plen > slen:
            return "-1"
        
        min_len = float('inf')
        start = 0
        start_index = -1
        hashs = [0] * 256
        hashp = [0] * 256
        count = 0
        
        for c in p:
            hashp[ord(c)] += 1 
        
        for i in range(slen):
            hashs[ord(s[i])] += 1
            
            if hashp[ord(s[i])] != 0 and hashs[ord(s[i])] <= hashp[ord(s[i])]:
                count += 1
            
            if count == plen:
                while hashs[ord(s[start])] > hashp[ord(s[start])] or hashp[ord(s[start])] == 0:
                    if hashs[ord(s[start])] > hashp[ord(s[start])]:
                        hashs[ord(s[start])] -= 1
                    start +=1 
                    
                lenn = i - start + 1
                if lenn < min_len:
                    min_len = lenn
                    start_index = start
                    
        if start_index == -1:
            return "-1"
        return s[start_index: start_index + min_len]
    
if __name__ == "__main__":  
    s = "ADOBECODEBANC"
    p = "ABC"
    sol = Solution()
    res = sol.minWindow(s, p)
    print(res)                 
            
            
            
            
        