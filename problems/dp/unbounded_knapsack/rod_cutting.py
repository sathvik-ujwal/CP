'''
Given a rod of length n(size of price) inches and an array of prices, price.
price[i] denotes the value of a piece of length i. Determine the maximum value 
obtainable by cutting up the rod and selling the pieces.

Input: price[] = [1, 5, 8, 9, 10, 17, 17, 20]
Output: 22
Explanation: The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5+17=22
'''

# very similar to 0/1 knapsack but instead of decrease the n while choosing the a element 
# you keep it the same as that element can be used again

class Solution:
    def cutRod(self, price):
        lengths = [i+1 for i in range(len(price))]
        dp = [[-1]*(len(price)+1) for _ in range(len(price)+1)]
        def knapsack(price, lengths, n, l):
            if n == 0 or l == 0:
                return 0
                
            if dp[n][l] != -1:
                return dp[n][l]
            if lengths[n-1] <= l:
                dp[n][l]  = max(price[n-1] + knapsack(price, lengths, n, l - lengths[n-1]), 
                knapsack(price, lengths, n-1, l))
            else:
                dp[n][l]= knapsack(price, lengths, n-1, l)
            return dp[n][l]
        
        return knapsack(price, lengths, len(price), len(price))
