'''
Approach 1: Lazy Deletion (Common Approach)

Every time a key's value changes, push the new (priority, key) pair into the heap.

Keep a dictionary latest[key] = value to store the latest value.

When popping the top, ignore stale entries by checking against latest.
'''


import heapq

heap = []
latest = {}

def update(key, value):
    latest[key] = value
    heapq.heappush(heap, (-value, key))  # max-heap using negative values

def get_top():
    while heap:
        value, key = heap[0]
        value = -value
        if latest[key] == value:  # valid entry
            return key, value
        heapq.heappop(heap)  # stale entry, remove
    return None
