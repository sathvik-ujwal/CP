# Meeting Rooms 2

'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
(si < ei), find the minimum number of conference rooms required.
'''

from heapq import heappush, heappop
class Solution:
    def meeting_rooms(self, arr: list[list[int]]) -> int:
        arr.sort()
        heap = []
        res = 0
        for i in range(len(arr)):
            start, end = arr[i][0], arr[i][1]
            if not heap:
                heappush(heap, end)
            else:
                while heap and heap[0] <= start:
                    heappop(heap)
                heappush(heap, end)

            res = max(res, len(heap))
        return res


sol = Solution()
arr = [[7,10],[2,4]]
res = sol.meeting_rooms(arr)
print(res)