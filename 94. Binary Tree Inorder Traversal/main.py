# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        myList = []
        def inOrder( root, ll):
            if not root:
                return None
            inOrder(root.left, ll)
            ll.append(root.val)
            inOrder(root.right, ll)
        inOrder(root, myList)
        return myList

        
