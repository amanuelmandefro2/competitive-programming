# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def divide_conquer(arr):
            if len(arr) < 1:
                return 
            max_idx = 0
            for i in range(1, len(arr)):
                if arr[i] > arr[max_idx]:
                    max_idx = i
            node = TreeNode(arr[max_idx])
            node.left = divide_conquer(arr[:max_idx])
            node.right = divide_conquer(arr[max_idx+1:])
            return node 
        return divide_conquer(nums)               

        