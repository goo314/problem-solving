"""LongestPanlindrome

Algorithm : 
    DFS
Level :
    Easy
Status :
    Accepted

Mon Nov 27 23:39:44 PST 2023
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result = None
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.result = None

        self.dfs(cloned, target)

        return self.result
    
    def dfs(self, node, target):
        if not node:
            return
        
        if node.val == target.val:
            self.result = node
            return
        
        self.dfs(node.left, target)
        self.dfs(node.right, target)