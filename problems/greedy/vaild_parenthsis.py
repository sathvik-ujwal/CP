'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        lstack = []
        sstack = []

        for i in range(len(s)):
            if s[i] == "(":
                lstack.append(i)
            elif s[i] == "*":
                sstack.append(i)
            else:
                if not lstack and not sstack:
                    return False
                if lstack:
                    lstack.pop()
                else:
                    sstack.pop()

        if lstack and not sstack or len(lstack) > len(sstack):
            return False
        if not lstack:
            return True
        if lstack and sstack:
            while lstack:
                if lstack[-1] > sstack[-1]:
                    return False
                lstack.pop()
                sstack.pop()
        return True
  

# linear time and space complexity  
    
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmax , leftmin = 0,0
        for i in range(len(s)):
            if s[i] == "(":
                leftmax += 1
                leftmin += 1
            elif s[i] == ")":
                leftmax -= 1
                leftmin -=1 
            else:
                leftmax += 1
                leftmin -= 1
            if leftmax < 0:
                return False
            if leftmin < 0:
                leftmin = 0
        return leftmin == 0