# Strobogrammatic Number III
'''
A strobogrammatic number is a number that looks the same 
when rotated 180 degrees (looked at upside down).

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.
'''

class Solution:
    def strobogrammatic_between(self, low: int, high: int) -> int:
        self.limit = len(str(high))
        self.low = low 
        self.high = high
        self.res = 0
        self.build(self.limit)
        self.build(self.limit-1)
        return self.res

    def build(self, n):
        if n == 0:
            return [""]
        if n == 1:
            temp = ["0", "1", "8"]
            for t in temp:
                if self.high >= int(t) >=  self.low:
                    self.res += 1
            return temp 

        temp_arr = self.build(n-2)
        pairs = [("0","0"), ("6","9"),("9","6"),("1","1"),("8","8")]

        new_array = []

        for num in temp_arr:
            for a,b in pairs:
                if a == "0" and len(num) == self.limit-2:
                    continue
                new = a+num+b
                if self.high >= int(new) >=  self.low:
                    self.res += 1

                new_array.append(new)
        return new_array
        

sol = Solution()
print("Enter low")
low = input()
print("Enter high")
high = input()
result = sol.strobogrammatic_between(int(low), int(high))
print(result)