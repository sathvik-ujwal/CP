# Strobogrammatic Number II
'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.
'''

class Solution:
    def strobogrammatic_number2(self, n: int) -> list[str]:
        res = ["1", "8", "6", "9"]
        same = {"0", "1", "8"}
        flip = {"6", "9"}
        tot = same | flip

        
        for i in range(1,n//2):
            temp = []
            for num in tot:
                for number in res:
                    temp.append(number+num)
            res = temp[:]

        if n % 2 != 0:
            temp = []
            for num in same:
                for number in res:
                    rev = list(number[::-1])
                    for i, r in enumerate(rev):
                        if r == "9":
                            rev[i] = "6"
                        elif r == "6":
                            rev[i] = "9"
                    
                    temp.append(number+num+"".join(rev))
            res = temp[:]
        else:
            temp = []
            for number in res:
                rev = list(number[::-1])
                for i, r in enumerate(rev):
                    if r == "9":
                        rev[i] = "6"
                    elif r == "6":
                        rev[i] = "9"
                    
                temp.append(number+"".join(rev))
            res = temp[:]

        return res 

    def recursive_strobo(self, n: int) -> list[str]:
        self.limit = n
        return self._build(n)

    def _build(self, n):
        if n == 0:
            return [""]
        if n == 1:
            return ["0", "1", "8"]

        temp = self._build(n-2)

        pairs = [("1","1"),("8","8"),("0","0"),("6","9"),("9","6")]

        new = []
        for num in temp:
            for a, b in pairs:
                if a == "0" and len(num) == self.limit-2:
                    continue
                new.append(a+num+b)

        return new 
            
        

sol = Solution()
n = 4
result = sol.strobogrammatic_number2(n)
result2 = sol.recursive_strobo(n)
print(result)
print(result2)