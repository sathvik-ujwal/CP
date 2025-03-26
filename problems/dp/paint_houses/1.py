'''
You have been given ‘N’ houses, each house can be painted with any of three colours:
green, red and yellow. You are also given a “cost” matrix of ‘N’ * 3 dimension which 
represents the cost of painting an i-th house (0-th based indexing) with j-th colour. 
The colour code is as follows: green - 0, red - 1 and yellow - 2. Now, you are supposed 
to find the minimum cost of painting all houses such that no adjacent houses are painted 
with the same colour.
'''

def minCost(cost):
    dp = [[0]*3 for _ in range(len(cost))]
    for i in range(3):
        dp[0][i] =  cost[0][i]
    for i in range(1, len(cost)):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][2], dp[i-1][0])
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])
    return min(dp[-1][0], dp[-1][1], dp[-1][2])   






