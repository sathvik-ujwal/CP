from typing import List, Optional
class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val =val
        self.left = left
        self.right =right
        
class ConstructFromPrePost:
    def buildTree(self, preorder: List[int], postorder: List[int]) -> Optional[Treenode]:
        if not postorder:
            return None
        val  =postorder.pop()
        node = Treenode(val)
        if not postorder:
            return node
        i = postorder.index(preorder[1])
        node.left = self.buildTree(preorder[1:i+2], postorder[:i+1])
        node.right = self.buildTree(preorder[i+2:], postorder[i+1:])
        
        return node
    
def preorderTraversal(root: Treenode) -> None:
    if not root:
        return
    print(root.val)
    preorderTraversal(root.left)
    preorderTraversal(root.right)
    return
        
if __name__ == "__main__":
    preorder = [1,2,4,5,3,6,7]
    postorder = [4,5,2,6,7,3,1]
    
    TreeBuilder = ConstructFromPrePost()
    root = TreeBuilder.buildTree(preorder, postorder)
    
    preorderTraversal(root)
    

    