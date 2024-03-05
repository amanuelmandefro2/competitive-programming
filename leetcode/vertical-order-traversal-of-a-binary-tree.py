# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_val = defaultdict(list)
        _min, _max = float('inf'), -float('inf')
        def traverse(root, c, d):
            if root:
                nonlocal _max,_min
                col_val[(d,c)].append(root.val)
                _max = max(_max, c)
                _min = min(_min, c)
                traverse(root.left, c-1, d+1)
                traverse(root.right, c+1, d+1)
        traverse(root, 0, 0)

        col_val = dict(sorted( col_val.items(), key=lambda item: item[0]))
        ans = [[] for _ in range(_max - _min+1)]


        for key in col_val:
            curr_arr = col_val[key]
            curr_arr.sort()
            ans[key[1]-_min].extend(curr_arr)
   
 



        return ans        