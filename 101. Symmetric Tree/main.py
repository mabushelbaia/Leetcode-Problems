# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def Symmetric(left, right):
            if( left != None and right == None ) or (left == None and right != None):
                return False
            if left == right == None:
                return True
            if left.val  != right.val:
                return False
            return(Symmetric(left.left, right.right) and Symmetric(left.right, right.left))
        return Symmetric(root.left, root.right)