#Course Schedule II 210
'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers,
return any of them. If it is impossible to finish all courses, return an empty array.

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
course 0. So the correct course order is [0,1].
'''

from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]

        for d, s in prerequisites:
            graph[s].append(d)
            indegree[d] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        res = []

        while q:
            prereq = q.popleft()
            res.append(prereq)

            for course in graph[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        if len(res) == numCourses:
            return res
        return []
    
    
## dfs sol
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
       
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        output = []
        visited, cycle = set(), set()

        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True

            cycle.add(c)
            for crs in graph[c]:
                if dfs(crs) == False:
                    return False

            cycle.remove(c)
            visited.add(c)
            output.append(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output

        
                    

         
        