import heapq
# dijstra
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for s, d ,w in times:
            graph[s].append((d, w))

        min_heap = [(0, k)]
        visited = set()
        t = 0
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)
            for n2, w2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1 + w2, n2))

        return t if len(visited) == n else -1