# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = -float('inf')
        def dfs(root, min_val, max_val):
            if not root:
                return 
            min_val = min(min_val, root.val)
            max_val = max(max_val, root.val)
            nonlocal ans
            ans = max(ans, max_val - min_val)
            dfs(root.left, min_val, max_val)
            dfs(root.right, min_val , max_val)
        dfs(root, root.val,root.val)
        return ans                   




        # _min_max = defaultdict(list)
        # _min, _max = float('inf'), -float('inf')
        # def max_min(root):
        #     if not root:
        #         return 
        #     nonlocal  _min, _max
        #     _min = min(_min, root.val)
        #     _max = max(_max, root.val)
        #     _min_max[root.val] = [_min, _max]
        #     max_min(root.left)
        #     _min = _min_max[root.val][0]
        #     _max = _min_max[root.val][1]
        #     max_min(root.right)
        # max_min(root)
        # max_diff = -float('inf')
        # for key in _min_max:
        #     max_diff = max(max_diff, _min_max[key][1] - _min_max[key][0])
        # return max_diff    

###48 minute
            
        