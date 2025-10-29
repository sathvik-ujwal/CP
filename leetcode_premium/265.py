# paint houses 2
''' 
k colors
'''


class Solution:
    def paint_houses(self, costs: list[list[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        dp = [[float('inf')]*k for _ in range(n)]

        first, second = float('inf'), float('inf')
        first_index, second_index = -1, -1

        for i in range(n):
            
            cost = costs[i]
            for j in range(k):
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

                
                
                
                


