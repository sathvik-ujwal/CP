# Factor combinations

'''
Numbers can be regarded as product of its factors. For example,
8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
'''

class Solution:
    def factors(self, n: int) -> list[list[int]]:
        self.number = n
        self.res = []
        self.recursion(n, 2, [])
        return self.res
    
    def recursion(self, n: int, fact: int, curr: list[int]) -> list[list[int]]:
        if n == 1:
            self.res.append(curr[:])
            return 
        if n <= 1 or fact >= self.number:
            return 
        
        self.recursion(n, fact+1, curr)
        if n % fact == 0:
            self.recursion(n//fact, fact, curr + [fact])
        return 


sol = Solution()
n = 9
res = sol.factors(n)
print("n:", n)
print(res)