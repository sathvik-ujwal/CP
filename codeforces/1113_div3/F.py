import sys
import math
import itertools
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from functools import lru_cache
from typing import List, Tuple
import time

input = sys.stdin.readline

# returns list input
def il():
    return list(map(int, input().split()))
    
# input matrix
def im():
    return [list(map(int, input().split())) for _ in range(int(input()))]
    
def pint(n):
    sys.stdout.write(str(n) + "\n")
    
def plist(l):
    sys.stdout.write(" ".join(map(str,l)) + "\n")
    
def solve():
    n,m,k =map(int. input().split())
    grid = [input() for i in range(n)]
    dp = [[0]*n for _ in range(m) for _ in range(2)]  
    
    # first iterate through the first row 
    # for all X 
    
    def dist(a,b,x,y):
        return math.sqrt((a-x)**2 + (b-y)**2)
    
    for i in range(n-1,-1, 0):
        for j in range(m):
            if grid[i][0][j] == "X":
                for l in range(k):
                    if i == n-1:
                        if j+l < m and grid[i][0][j+l] == "X":
                            dp[i][j-l][1] += 1 
                        if j-l >= 0 and grid[i][0][j-l] == "X":
                            dp[i][j+l][1] += 1 
                            
                    else:
                        if grid[i][0][j]=="X":
                            if dist(1, j, 0, j-l) <= k:
                                if j+l < m:
                                    dp[i][j][0] = dp[i+1][j+l][0] + dp[i+1][j+l][1]
                                if j-l >= 0:
                                    dp[i][j][0] = dp[i+1][j-l][0] + dp[i+1][j-l][1]
                                    
                        if j+l < m and grid[i][0][j+l] == "X":
                            dp[i][j-l][1] += 1 
                        if j-l >= 0 and grid[i][0][j-l] == "X":
                            dp[i][j+l][1] += 1 
    res = 0
    for i in range(m):
        for j in range(2):
            if grid[0][i] == "X":
                res += dp[0][i][j]
    print(res)
    return
    
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
    

    
    