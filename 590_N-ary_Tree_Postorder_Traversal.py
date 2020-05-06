#590. N-ary Tree Postorder Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = []
        res =[]
        stack.append(root) 
        while stack:
            node = stack.pop() #node = [5]
            res.append(node.val) #res = [1,3,5]
            stack.extend(node.children) #stack = [4,2,6]
        return res[::-1]

        #recursive way
        # """
        # # Definition for a Node.
        # class Node:
        #     def __init__(self, val=None, children=None):
        #         self.val = val
        #         self.children = children
        # """

        # class Solution:
        #     def postorder(self, root: 'Node') -> List[int]:

        #         res =[]
        #         if not root:
        #             return res
        #         for child in root.children:
        #             res.extend(self.postorder(child))
        #         res.append(root.val)
        #         return res