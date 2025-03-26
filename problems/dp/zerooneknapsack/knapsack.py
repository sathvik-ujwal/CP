'''
given weights and values. you have to maximize the value you can put in the bag
while ensuring the weight does not exceed the given number.

3 types
unbounded (dp) -> same item can be added multiple times
0/1 (dp) -> fractions cant be added
fractional knapsack (greedy) -> where a fraction of a weight can be added

'''

# 0/1
# how to identify knapsack ?
# when ever you are given an array elements and you have to decide whether to take an element
# or not while making sure we dont exceed or a given number and so on

# template

def knapsack_recursion(weights, values, w, n):
    # base condition
    if n == 0 or w == 0:
        return 0
    if weights[n-1] <= w:
        return max(values[n-1] + knapsack_recursion(weights, values, w - weights[n-1], n-1) 
                   , knapsack_recursion(weights, values, w, n-1))
    else:
        return knapsack_recursion(weights, values, w, n-1)
    
    
def memoization(weights, values, w, n):
    # the variables used for the dimensions of thr matrix should be in ones that
    # change during the recursion calls
    # the basic idea is to store all the results for each recursive and
    # if it's already stored return it without further recursize calls
    # since we only have to fill the w*n matrix
    # time complexity : O(n^2)
    # space complexity : O(n^2)
    
    # the index [w][n] in the matrix is the maximum res if the weight is w and 
    # only the first n elements are considered 
    # this way be break down the problem into smaller subproblems
    
    dp = [[-1]*(n+1) for _ in range(w+1)]
    
    def recursion(weights, values, w, n):
        if n == 0 or w == 0:
            return 0
        if dp[w][n] != -1:
            return dp[w][n]
        if weights[n-1] <= w:
            dp[w][n] = max(values[n-1] + recursion(weights, values, w - weights[n-1], n-1), recursion(weights, values, w, n-1))
        else:
            dp[w][n] = recursion(weights, values, w, n-1)
        
        return dp[w][n]
    recursion(weights, values, w, n)
    return dp[-1][-1]

def topDownApproach(weights, values, w, n):
    # here we begin from the start ie when w is 0 and no of values ie n is 0 to the end
    # to get the base case for the dp matrix initialization we look at the base case of 
    # our recursive function where it says the for n == 0 or w == 0 return 0
    # so we initialize the first row and column as 0s
    
    dp = [[-1]*(n+1) for _ in range(w+1)]
    for i in range(w+1):
        dp[i][0] = 0
    for i in range(n+1):
        dp[0][i] = 0
        
    # then we try to replicate the recursive function calls to fill the dp matrix
    
    for i in range(1, w+1):
        for j in range(1, n+1):
            if weights[j-1] <= w:
                dp[i][j] = max(values[j-1] + dp[i-weights[j-1]][j-1], dp[i][j-1])
            else:
                dp[j][j] = dp[i][j-1]
    return dp[-1][-1]
                
                
        
    

if __name__ == "__main__" :
    weights = [1,2,3,4]
    values = [3,4,5,8]
    w = 7
    
    res = topDownApproach(weights, values, w, len(weights))
    print(res)
                             
        