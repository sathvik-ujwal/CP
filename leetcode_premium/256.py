# paint house

'''
There are a row of n houses, each house can be painted with one of the three colors: red, blue 
or green. The cost of painting each house with a certain color is different. You have to paint 
all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the
cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.
'''

class Solution:
    def paint_houses(self, costs: list[list[int]]) -> int:
        n = len(costs)
        dp = [[float('inf')]*3 for _ in range(n)]

        first, second = float('inf'), float('inf')
        first_index, second_index = -1, -1

        for i in range(n):
            
            cost = costs[i]
            for j in range(3):
                dp[i][j] = costs[i][j]
                if first != float('inf'):
                    dp[i][j] += first if j != first_index else second
               

            first, second = float('inf'), float('inf')
            first_index, second_index = -1, -1

            for j,color in enumerate(dp[i]):
                if color <= first:
                    second = first 
                    second_index = first_index
                    first = color
                    first_index = j
                elif color < second:
                    second = color 
                    second_index = j
          
        return min(dp[-1])

sol = Solution()
costs = [[17,2,17],[16,16,5],[14,3,19]]
res = sol.paint_houses(costs)
print(res)

                
                
                
                


