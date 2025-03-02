# 2467 Most profitable path
'''
There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 
2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between 
nodes ai and bi in the tree.

At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:

the price needed to open the gate at node i, if amount[i] is negative, or,
the cash reward obtained on opening the gate at node i, otherwise.
The game goes on as follows:

Initially, Alice is at node 0 and Bob is at node bob.
At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves towards node 0.
For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
If the gate is already open, no price will be required, nor will there be any cash reward.
If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other words, 
if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both 
of them receive c / 2 each.
If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events 
are independent of each other.
Return the maximum net income Alice can have if she travels towards the optimal leaf node.
'''

# d0 is the distance of alice from the node that is distance of node from 0
# db is bobs distance from that node
# if db > d0 then add the whole amount 
# if db == d0 then add half the amount
# else dont add anything

def mostProfitablePath(edges, bob, amount):
    n = len(edges) + 1
    tree = [[] for i in range(n)]
    for n1,n2 in edges:
        tree[n1].append(n2)
        tree[n2].append(n1)
        
    seen = [0] * n
    
    def dfs(node, d0):
        seen[node] = 1
        db = 0 if node == bob else n
        res = float('-inf')
        
        for child in tree[node]:
            if seen[child] == 1:
                continue
            
            temp_res, bob_dist = dfs(child, d0+1)
            res = max(res, temp_res)
            db = min(db, bob_dist)
        if res == float('-inf'):
            res = 0
        if db == d0:
            res += amount[node] // 2
        if db > d0:
            res += amount[node]
        
        return res, db+1
            
            
        