# Sliding window maximum
'''
You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. You can 
only see the k numbers in the window. Each time the sliding window moves right 
by one position.
Return the max sliding window.
'''

from heapq import heappush, heappop
from sortedcontainers import SortedList

# using min heap (priority queue) time complexity O(nlogn) space O(n)
def minWindow(nums, k):
    ans = []
    heap = []
    
    for i in range(k):
        heappush(heap, (-nums[i], i))
        
    ans.append(-heap[0][0])
    
    for i in range(k, len(nums)):
        heappush(heap, (-nums[i], i))
        
        while heap[0][-1] <= i - k:
            heappop(heap)
        
        ans.append(-heap[0][0])
    
    return ans

# using deque.ie double sided queue
# while inserting an element into the deque remove all the elements in the queue smaller than 
# it as they wont be need any further

from collections import deque

def minWindowval(nums, k):
    ans = []
    dq = deque()
    
    for i in range(k):
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
            
        dq.append(i)
        
    ans.append(nums[dq[-1]])
    
    for i in range(k, len(nums)):
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        while dq and dq[0] <= i - k:
            dq.popleft()
            
        dq.append(i)
        ans.append(nums[dq[-1]])
        
    
        
    
    