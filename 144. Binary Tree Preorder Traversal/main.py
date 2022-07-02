# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        myList = []
        def preOrder( root, ll):
            if not root:
                return None
            ll.append(root.val)
            preOrder(root.left, ll)
            preOrder(root.right, ll)
        preOrder(root, myList)
        return myList