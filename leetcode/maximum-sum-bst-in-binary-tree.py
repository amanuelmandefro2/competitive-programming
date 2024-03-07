# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def bst(root):
            if not root:
                return [float('inf'), -float('inf'), 0]
            nonlocal ans
            l_min, l_max, l_sum = bst(root.left)
            r_min, r_max, r_sum = bst(root.right)
            if l_max >= root.val or root.val >= r_min:
                return [-float('inf'), float('inf'), 0]
            _sum = l_sum + r_sum + root.val   
            ans = max(_sum, ans)

            return [min(root.val, l_min), max(root.val, r_max), _sum]  

        bst(root)      
                 
        return ans         
        