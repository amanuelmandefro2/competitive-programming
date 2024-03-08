# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def inorder(root):
            if root:
                inorder(root.left)
                nums.append(root.val)
                inorder(root.right)
        inorder(root)        
        def divide_conquer(l, r):
            if l > r:
                return 
            mid = (l+r)//2
            node = TreeNode(nums[mid])
            node.left = divide_conquer(l, mid-1)
            node.right = divide_conquer(mid+1, r)
            return node

        return divide_conquer(0, len(nums)-1)        

        