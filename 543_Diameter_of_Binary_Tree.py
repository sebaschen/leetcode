#543
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def diameterOfBinaryTree(self, root):
        diameter = [0]
        self.depth(root, diameter)
        return diameter[0]

    def depth(self, root, diameter):
        if not root:
            return 0
        left_height = self.depth(root.left, diameter)
        right_height = self.depth(root.right, diameter)
        diameter[0] = max(diameter[0], left_height + right_height)
        return 1 + max(left_height, right_height)