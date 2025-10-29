'''
Given a binary tree where all the right nodes are either leaf 
nodes with a sibling (a left node that shares the same parent node) 
or empty, flip it upside down and turn it into a tree where the original right 
nodes turned into left leaf nodes. Return the new root.
'''
from collections import deque

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None 
        self.right = None 

class Solution:
    def upside_down(self, root: TreeNode) -> TreeNode:
        par = root

        if not root.left:
            return root
        par = self.upside_down(root.left)

        left = root.left 
        right = root.right 
        left.left = right 
        left.right = root 
        root.left, root.right = None, None

        return par

    def print_tree(self, root: TreeNode):
        q = deque()
        q.append(root)
        res = []
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        print(res)
        return res


    #def using_extra(self, root: TreeNode) -> TreeNode:
    #    arr = []
    #    def build(root):
    #        if not root:
    #            return  
    #        left = root.left
    #        right = root.right 
    #        

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol.print_tree(root)
new_root = sol.upside_down(root)
sol.print_tree(new_root)


        
        


    
