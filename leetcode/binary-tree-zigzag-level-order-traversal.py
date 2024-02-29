# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_value = defaultdict(list)
        def preorder(root, c):
            if root:
                level_value[c].append(root.val)
                preorder(root.left, c+1)
                preorder(root.right, c+1)
        preorder(root, 0)
        ans = []
        for level in level_value:
            if level%2:
                ans.append(level_value[level][::-1])
            else:
                ans.append(level_value[level])            
                
        return ans         