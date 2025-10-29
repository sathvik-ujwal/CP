#Missing Ranges
'''
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
'''


class Solution:
    def missing_ranges(self, nums: list[int], upper: int, lower: int) -> list[str]:
        if nums[0] != lower:
            nums.insert(0, lower)
        if nums[-1] != upper:
            nums.append(upper)

        res = []

        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                continue
            if nums[i+1]-nums[i] == 2:
                res.append(str(nums[i]+1))
            else:
                res.append(str(nums[i])+"->"+str(nums[i+1]))
        return res
    
sol = Solution()
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 100
result = sol.missing_ranges(nums, upper, lower)
print(result)
