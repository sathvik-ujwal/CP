'''
The Shortest Path Faster Algorithm (SPFA) is an optimized version of
the Bellman-Ford algorithm for finding the shortest paths from a single
source to all other vertices in a graph. It uses a queue-based approach to reduce 
unnecessary edge relaxations, often making it faster in practice.

SPFA improves on Bellman-Ford by maintaining a queue of vertices that might lead 
to distance improvements when their outgoing edges are relaxed. Instead of relaxing
all edges in each iteration (as in Bellman-Ford), SPFA only processes the vertices 
that are actively part of shortest path updates.
'''

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for s, d, w in times:
            adj[s].append((d, w))

        dist = {node: float('inf') for node in range(1, n+1)}
        q = deque([(k,0)])
        dist[k] = 0

        while q:
            node, time = q.popleft()
            if dist[node] < time:
                continue
            for neigh, w in adj[node]:
                if time + w < dist[neigh]:
                    dist[neigh] = time + w
                    q.append((neigh, time + w))

        res = max(dist.values())
        return res if res != float('inf') else -1


