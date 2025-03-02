# 295 Find Median from data stream

from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heappush(self.large, num)
        else:
            heappush(self.small, -num)

        if len(self.small) > len(self.large) + 1:
            val = -heappop(self.small)
            heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush(self.small, -val)

    

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0])/2.0
        