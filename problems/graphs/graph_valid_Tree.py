# graoh valid tree
'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.
'''

# dfs

from typing import List
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        Tree = defaultdict(list)

        for p, c in edges:
            Tree[p].append(c)
            Tree[c].append(p)

        visited = set()
        connected = set()

        def dfs(node, par):
            if node in visited:
                return False
            visited.add(node)
            for child in Tree[node]:
                if child == par:
                    continue
                if dfs(child, node) == False:
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
        # indegree 


        