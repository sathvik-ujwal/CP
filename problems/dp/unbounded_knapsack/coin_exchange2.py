'''
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that 
amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer
'''

from typing import List
# recursion O(2^n)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def recursion(coins, a, n):
            if n == 0:
                return 0
            
            if a == 0:
                return 1

            if coins[n-1] <= a:
                return recursion(coins, a-coins[n-1], n) + recursion(coins, a, n-1)
            else:
                return recursion(coins, a, n-1)
            
        return recursion(coins, amount, len(coins))
            
# Memoization O(n*amount)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def recursion(coins, a, n):
            if n == 0:
                return 0
            
            if a == 0:
                return 1
            
            if (n, a) in dp:
                return dp[(n, a)]

            if coins[n-1] <= a:
                dp[(n,a)] = recursion(coins, a-coins[n-1], n) + recursion(coins, a, n-1)
            else:
                dp[(n, a)]  = recursion(coins, a, n-1)
            return dp[(n, a)]
            
        return recursion(coins, amount ,len(coins))
            
# dynamic programming 
# TC- O(n*amount)
# ST- O(amount)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = dp[i-coin] + dp[i]
        return dp[amount]
   