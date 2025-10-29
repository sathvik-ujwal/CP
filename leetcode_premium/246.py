#Strobogrammatic number
'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
'''

class Solution:
    def strobogrammatic_number(self, num: str) -> bool:
        l, r = 0, len(num)-1
        stro = {"1", "8", "0"}
        strobo = {"6", "9"}

        while l <= r:
            if l == r:
                if num[l] in stro:
                    return True
                return False 
            if num[l] == num[r] and num[l] not in stro:
                return False 
            if num[l] != num[r] and (num[l] not in strobo or num[r] not in strobo):
                return False 
            l +=1
            r -= 1

        return True

sol = Solution()
num = "9880886"
res = sol.strobogrammatic_number(num)
print(res)
            