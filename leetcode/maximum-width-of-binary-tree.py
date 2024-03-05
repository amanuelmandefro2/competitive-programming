# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth_width = defaultdict(list)
        def trev(root, c, d):
            if root:
                # if c not in  depth_width:
                depth_width[c].append(d)   
                trev(root.left, c+1, 2*d+1)
                trev(root.right, c+1, 2*d+2)
        trev(root, 1, 0)
        max_width = -float('inf')

        for depth in depth_width:
            max_width = max(max_width, depth_width[depth][-1] - depth_width[depth][0]+1)



        # print(depth_width)
        return max_width    
        