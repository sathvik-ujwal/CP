'''
Ninja has started a painting business recently. He got a contract to paint ‘N’ 
houses in a city. Ninja has ‘K’ colors to choose from. But the client has a condition 
that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an N x K cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost 
of painting house 1 with color 2, and so on.

Your task is to help Ninja to find the minimum cost required to paint houses according to this condition.
'''

from os import *
from sys import *
from collections import *
from math import *

def paintCost(n, k, costs):   
    dp = costs[0]

    for i in range(1, n):
        min1, min2=float('inf'), float('inf')
        min_index = -1
        for j in range(k):
            if dp[j] < min1:
                min_index = j
                min2 = min1 
                min1 = dp[j]
            elif dp[j] < min2:
                min2 = dp[j]

        for j in range(k):
            if j == min_index:
                dp[j] = min2 + costs[i][j]
            else:
                dp[j] = min1 + costs[i][j]
    return min(dp)
    pass