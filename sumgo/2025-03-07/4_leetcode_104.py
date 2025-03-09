# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(cur, depth):
            if not cur:
                return depth-1
            return max(dfs(cur.left, depth+1), dfs(cur.right, depth+1))
        
        return dfs(root, 1)