# min heap is a specify type of priority queue
# The heap will not always be in the sorted order 
# but when poped it will return in the required order

from heapq import heapify, heappush, heappop
import heapq
from collections import defaultdict

priority_queue = []
heapify(priority_queue)

heappush(priority_queue, 32)
heappush(priority_queue, 44)
heappush(priority_queue, 4)
print(priority_queue)
heappush(priority_queue, 7)

print(priority_queue)
print(heappop(priority_queue))
print(priority_queue)

'''
[4, 7, 32, 44]
4
[7, 44, 32]
'''

# priority queue of lists where the second element is the decider

# Initialize a priority queue (min-heap)
priority_queue = []

# Push elements into the priority queue, using the second element as the priority
heapq.heappush(priority_queue, (3863937, [1, 3863937]))  # (priority, full item)
heapq.heappush(priority_queue, (1968030, [3, 1968030]))
heapq.heappush(priority_queue, (8937888, [7, 8937888]))

# Adding a new element
heapq.heappush(priority_queue, (543210, [2, 543210]))

# Pop elements in priority order
while priority_queue:
    _, item = heapq.heappop(priority_queue)  # Discard the priority key, keep the item
    print(item)
    
'''
[2, 543210]
[3, 1968030]
[1, 3863937]
[7, 8937888]

'''

# priority queue of lists where the first element is the decider

import heapq

# Initialize a priority queue (min-heap)
priority_queue = []

# Push elements into the priority queue
heapq.heappush(priority_queue, [1, 3863937])
heapq.heappush(priority_queue, [3, 1968030])
heapq.heappush(priority_queue, [7, 8937888])

# Adding a new element
heapq.heappush(priority_queue, [2, 543210])

# Pop elements in priority order
while priority_queue:
    print(heapq.heappop(priority_queue))

'''
[1, 3863937]
[2, 543210]
[3, 1968030]
[7, 8937888]

'''