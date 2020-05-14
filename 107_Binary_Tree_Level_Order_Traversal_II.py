# 107. Binary Tree Level Order Traversal II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return [ ]
        current, res =[root],[]
        while current:
            vals,next_level=[],[] #val儲存本層的node值,next_level儲存下層的node 
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level #current更新為下層node
            res.append(vals)        
        return res[::-1] #result要reverse過來