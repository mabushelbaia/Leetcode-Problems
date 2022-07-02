# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def same(a, b):
            if (not a and b) or ( not b and a):
                return False
            if not a and not b:
                return True
            if a.val == b.val:
                return same(a.left, b.left) and same(a.right, b.right)
            else:
                return False
        return same(p, q)