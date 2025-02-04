# Used to find the number of connected components in a graph

class UnionFind:
    def __init__(self,  n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
        self.n = n

    def find(self, node):
        
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        
        if p1 == p2:
            return 0
        
        if self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        return 1
    
    def connectedComponents(self, arr):
        count = self.n
        for n1,n2 in arr:
            count -= self.union(n1, n2)
            
        return count
        
        
                
if __name__ == "__main__":
    print("Enter the number of nodes")
    n = int(input())
    print("Enter the number of edges")
    edges_count = int(input())
    edges =[]
    print("Enter the edges")
    for _ in range(edges_count):
        edges.append(list(map(int, input().split())))
        
    res = UnionFind(n)
    print(res.connectedComponents(edges))
        
            
        