'''

given an array find the gcd such that
if array is [a, b, c]
sort the array such that sum of gcds is maximum
for example for [a, b, c] the gcds = [gcd(a), gcd(a, b), gcd(a, b, c)]

'''
from typing import List
from itertools import permutations
import time
import math
from math import gcd 
from heapq import heappush, heappop, heapify

class Solution:
    def getMaxGCDBruteForce(self, arr: List[int]) -> int:

        n = len(arr)
        res = 0

        def getPerm(arr):
            for p in permutations(arr):
                yield p

        for perm in getPerm(arr):
            curr = perm[0]
            temp = perm[0]
            for i in range(1, n):
                curr = math.gcd(curr, perm[i])
                temp += curr 
            res = max(res, temp)
                
        return res

    def Greedy(self, arr: List[int]) -> int:
        n = len(array)
        used = [False]*n

        index = max(range(n), key=lambda i: arr[i])
        curr_gcd = arr[index]
        used[index] = True
        total = curr_gcd


        for i in range(n-1):
            best = 0
            best_index = -1
            for j in range(n):
                if not used[j]:
                    temp_gcd = gcd(curr_gcd, arr[j])
                    if temp_gcd > best:
                        best = temp_gcd
                        best_index = j 

            used[best_index] = True
            total += best
            curr_gcd = best

        return total

    def greedyHeaps(self, arr: List[int]) -> int:
        n = len(array)
        
    

    


solution = Solution()
array = [6, 4, 8, 7, 12, 16, 20, 16]

start = time.perf_counter()
res = solution.getMaxGCDBruteForce(array)
end = time.perf_counter()
print(res)
print("Execution time for brute force:", end - start, "seconds")

start = time.perf_counter()
res = solution.Greedy(array)
end = time.perf_counter()
print(res)
print("Execution time for greedy :", end - start, "seconds")

