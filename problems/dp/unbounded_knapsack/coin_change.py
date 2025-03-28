'''
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def recursion(coins, a, n):
            if a == 0:
                return 0
            if n == 0:
                return amount+1
            
            if (a, n) in dp:
                return dp[(a, n)]

            if coins[n-1] <= a:
                dp[(a, n)] = min(1+recursion(coins, a-coins[n-1], n),
                recursion(coins, a, n-1))
            else:
                dp[(a, n)] = recursion(coins, a, n-1)

            return dp[(a, n)]
        res = recursion(coins, amount, len(coins))
        return res if res != amount + 1 else -1
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])

        return dp[amount] if dp[amount] != amount+1 else -1