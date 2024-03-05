# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def sum(root, ans):
            nonlocal res
            if not root:
                return 
            if not root.left and not root.right:
                res += ans*10 + root.val
                return 
            sum(root.left, ans*10+root.val)
            sum(root.right, ans*10+root.val)
        sum(root, 0)
        return res    

        