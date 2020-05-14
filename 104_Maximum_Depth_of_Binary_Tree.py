# 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
#   rescursive method
#         res = [ ]
#         x =0
#         self.helper(root, res,x)
#         if len(res) !=0:
#             return max(res)
#         return 0 
            
#     def helper(self,root,res,x):        
#         if root:
#             x+=1
#             self.helper(root.left, res,x)
#             self.helper(root.right, res,x)
#             res.append(x)
