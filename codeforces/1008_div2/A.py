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
    n, t =map(int,input().split())
    a = il()
    if sum(a)%n == 0 and sum(a)//n == t:
        print("YES")
    else:
        print("NO")   
    return
        
    
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
    

    
    