#144. Binary Tree Preorder Traversal
class Solution:
    # recursively
    def preorderTraversal(self, root):
        res = [ ]
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

