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
    n, m = map(int, input().split())
    if m == 1 and n != 2:
        plist([i for i in range(1, n)]+[n-1])
    else:
        if n == 2:
            if m % 2 == 0:
                plist([1,2])
            else:
                plist([2,1])
        else:
            if m % 2 == 0:
                plist([n-1]*(n-1) + [n])
            else:
                plist([n]*[n-1] + [n-1])
    return
        
    
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
    

    
    