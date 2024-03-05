# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        def DFS(root):
            if root:
                freq[root.val] += 1
                DFS(root.left)
                DFS(root.right)
        DFS(root)        
        mode = max(list(freq.values()))
        ans = []
        for key in freq:
            if freq[key] == mode:
                ans.append(key)

        return ans        
        