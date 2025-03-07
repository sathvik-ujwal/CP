'''
The Bellman-Ford algorithm is used to find the shortest paths from a 
single source vertex to all other vertices in a weighted graph. It works 
for graphs with negative edge weights and can also detect negative weight cycles.


When to Use

Bellman-Ford:
When you need to compute shortest paths from a single source.
Suitable for graphs with negative edge weights.
Efficient for sparse graphs (graphs with fewer edges).

Floyd-Warshall:
When you need to compute shortest paths between all pairs of vertices.
Typically used for dense graphs (graphs with many edges).


Key Idea: Shortest Path in a Graph
In any graph, the shortest path between two vertices contains at most V-1 edges.
This is becuse a path cannot visit more than  V vertices without revisiting one,
which would form a cycle (and shortest paths do not include cycles unless it's a negative cycle).

If there are no negative weight cycles, further relaxations will not change the distances because 
all shortest paths are already correct.
If there are negative weight cycles, further relaxations will continue to decrease distances 
indefinitely. This is how the algorithm detects negative cycles.
'''

# leetcode 743
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf') for i in range(n)]
        print(dist)
        dist[k-1] = 0

        for _ in range(n-1):
            for s, d, w in times:
                if dist[s-1] + w < dist[d-1]:
                    dist[d-1] = dist[s-1] + w

        res = max(dist)
        return res if res != float('inf') else -1
