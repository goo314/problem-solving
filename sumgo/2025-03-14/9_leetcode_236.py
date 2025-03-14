# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(x):
            if not x:
                return
            if x == p or x == q:
                return x
            
            left = dfs(x.left)
            right = dfs(x.right)

            if left and right:
                return x
            elif left:
                return left
            else:
                right
        
        return dfs(root)