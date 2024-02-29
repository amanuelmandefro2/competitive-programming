# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor1 = []
        def ancestor(root, child):
            if root.val < child.val:
                return [root] + ancestor(root.right, child)
            elif root.val > child.val:
                return [root] + ancestor(root.left, child)
            else:
                return [root] 
        ancestor1 = ancestor(root, p)
        ancestor2 = ancestor(root, q)
        # min_anc = 
        print(root)
        ancestor2 = set(ancestor2)
        common_anc = []
        # print(ancestor2, ancestor1)
        for anc in ancestor1:
            if anc in ancestor2:
                common_anc.append(anc)
       
               
        return common_anc[-1] 
      

