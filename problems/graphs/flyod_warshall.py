'''
Shortest Path in a Directed Graph:
Find the shortest paths between all pairs of vertices in a weighted directed graph.

Negative Cycle Detection:
Check if a graph contains any negative weight cycles. If 
dist[i][i]<0 after execution, there is a negative cycle.

Transitive Closure of a Graph:
Use Floyd-Warshall to compute the transitive closure, which tells whether a path exists between any two vertices.

Find the Diameter of a Graph:
The diameter is the maximum shortest path length in the graph (assuming no disconnected components).

All-Pairs Minimum Cost in Road Networks:
Given a network of roads with toll costs, find the minimum cost to travel between all pairs of cities.

Path Reconstruction:
Reconstruct the shortest path between two vertices after running the algorithm using a parent or next matrix.

Network Reliability Analysis:
Use Floyd-Warshall to analyze or improve network reliability by computing shortest paths and making optimizations.

Find the Center of the Graph:
Identify the node with the minimum of the maximum shortest path distance to all other nodes.

Optimal Meeting Point:
Find the node that minimizes the maximum travel distance for a group of people starting at different nodes.

Minimize Time to Pass a Message:
Use Floyd-Warshall to determine the quickest time required to broadcast a message to all nodes in a network.
'''

# The Floyd-Warshall algorithm is a dynamic programming algorithm used to find the shortest 
# paths between all pairs of vertices in a weighted graph. It works for both directed and 
# undirected graphs and can handle graphs with negative edge weights (but not negative cycles).

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[float('inf')]*n for _ in range(n)]

        for s, d, w in times:
            graph[s-1][d-1] = w

        for i in range(n):
            graph[i][i] = 0

        for mid in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][mid] + graph[mid][j])

        res = max(graph[k-1])
        return res if res != float('inf') else -1
