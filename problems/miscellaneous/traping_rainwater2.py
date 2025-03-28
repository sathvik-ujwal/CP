# trap water in 2 d grid of heights

# 3 4 4 5 
# 4 5 1 5
# 4 1 3 4
# 4 4 4 4

from typing import List
from heapq import heappush, heappop


def trapRainWater(heightMap: List[List[int]]) -> int:
    rows, cols = len(heightMap), len(heightMap[0])
    visited = [[0]*(cols) for _ in range(rows)]
    heap = []
    
    for i in range(cols):
        heappush(heap, (heightMap[0][i], 0, i))
        heappush(heap, (heightMap[rows-1][i], rows-1, i))
        visited[0][i] = -1
        visited[rows-1][i] = -1
    for j in range(1, rows-1):
        heappush(heap, (heightMap[j][0], j, 0))
        heappush(heap, (heightMap[j][cols-1], j, cols-1))
        visited[j][0] = -1
        visited[j][cols-1] = -1
    res = 0
    max_h = -1
    while heap:
        h, r, c = heappop(heap)
        max_h = max(max_h, h)
        res += max_h - h
        neigh = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in neigh:
            nr , nc = r + dr, c + dc
            if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or visited[nr][nc] == -1):
                continue
            heappush(heap, (heightMap[nr][nc], nr, nc))
            visited[nr][nc] = -1
    return res

if __name__ == "__main__":
    grid = [[3,4,4,5], [4,5,1,5], [4,1,3,4], [4,4,4,4]]
    res = trapRainWater(grid)
    print(res)
