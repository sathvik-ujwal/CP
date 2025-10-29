# Meetings Rooms
'''
Given an array of meeting time intervals consisting of 
start and end times [[s1,e1],[s2,e2],...] (si < ei), determine 
if a person could attend all meetings.
'''

class Solution:
    def meeting_rooms(self, arr: list[list[int]]) -> bool:
        arr.sort()
        start = arr[0][0]
        end = arr[0][1]
        for i in range(1, len(arr)):
            curr_start, curr_end = arr[i][0], arr[i][1]
            if curr_start < end:
                return False 
            end = curr_end 

        return True
            
            

sol = Solution()
arr =  [[0,3],[5,10],[15,20]]
res = sol.meeting_rooms(arr)
print(res)

