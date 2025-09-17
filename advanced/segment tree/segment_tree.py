from typing import List

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0]*(n * self.n)
        self.build(arr, 1, 0, self.n-1)

    def build(self, arr, index, l, r):
        if l == r:
            self.tree[index] = arr[l]
            return
        
        mid = (l+r)//2
        self.build(arr, 2*index, l, mid)
        self.build(arr, 2*index+1, mid+1, r)
        self.tree[index] = self.tree[2*index] + self.tree[2*index+1]

        return 

    def query(self, index, )