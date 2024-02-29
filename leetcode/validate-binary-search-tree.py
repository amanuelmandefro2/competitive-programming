# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # print(root)
        ans = []
        def bst(root):
            if root:
                bst(root.left)
                ans.append(root.val)
                bst(root.right)
        bst(root)
        for i in range(len(ans)-1):
            if ans[i] >= ans[i+1]:
                return False
        print(ans)        
            # if not root:
            #     return True
           
            # elif  root.left and root.left.val >= root.val:
            #     return False
            # elif root.right and root.right.val <= root.val:
            #     return False
            # return bst(root.left) and bst(root.right)          

        return True

               
        