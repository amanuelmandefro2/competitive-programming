# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left, right = root.left, root.right
        def symmetric(left, right):
            if (not left and right) or (not right and left):
                return False
            elif left and right and left.val != right.val:
                return False
            elif left and right and  not symmetric(left.left, right.right):
                return False
            elif left and right and not symmetric(left.right, right.left):
                return False    
            return True 

        return symmetric(left, right)     
        