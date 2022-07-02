# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def LCA(root, a, b):
            if a.val < root.val and b.val < root.val and root.left:
                return LCA(root.left, a, b)
            if a.val > root.val and b.val > root.val and root.right:
                return LCA(root.right, a, b)
            else:
                return root
        return LCA(root, p, q)