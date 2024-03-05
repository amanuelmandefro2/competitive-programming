# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def sum(root, low, high):
            if root:
                nonlocal ans
                if low <= root.val <= high:
                    ans += root.val
                sum(root.left, low, high)
                sum(root.right, low, high) 
        sum(root, low, high)

        return ans           
