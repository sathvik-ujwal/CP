class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # heap -> [empty rooms]
        # dict / array -> track count of meetings held in each room
        # heap -> tracj meeints
      
        meetings.sort()
        
        
        heap1 = [i for i in range(n)]
        heapify(heap1)
        heap2 = []
        array = [0]*n

        for i in range(len(meetings)):
            
            if heap2:
                while heap2 and heap2[0][0] <= meetings[i][0]:
                    
                    curr = heappop(heap2)
                    heappush(heap1, curr[1])
            
            if heap1:
                curr = heappop(heap1)
                array[curr] += 1
                heappush(heap2, [meetings[i][1], curr])
            else:
                curr = heappop(heap2)
                array[curr[1]] += 1
                curr[0] = curr[0] + (meetings[i][1] - meetings[i][0])
                heappush(heap2, curr)
          
        res = float('-inf')
        index = -1
        for i in range(len(array)):
            if array[i] > res:
                res = array[i]
                index = i
        return index


            