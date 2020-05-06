"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        #iterative method 
        if not root:
            return []
        stack = []
        res = []
        stack.append(root) 
        while stack:#stack = []
            node = stack.pop() #node = [2]
            res.append(node.val) #res=[1,3,5,6,2,4]
            stack.extend(node.children[::-1]) #stack = []
        return res

# recursive method
#         res = []
#         if not root:
#             return res
#         res.append(root.val)
#         for child in root.children:
#             res.extend(self.preorder(child))
#         return res