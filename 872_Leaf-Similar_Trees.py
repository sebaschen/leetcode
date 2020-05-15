# 872_Leaf-Similar_Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.preorder(root1) == self.preorder(root2)
    
    def preorder(self,root):
        stack = []
        stack.append(root)
        res = []

        while stack:
            node = stack.pop()
            if not node: continue
            if not node.left and not node.right:                            
                res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)                
        return res
        
