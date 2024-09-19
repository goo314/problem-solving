"""LeetCode

Algorithm : 
    DFS
Level :
    Medium
Status :
    Accepted

Thu Nov 30 23:34:36 PST 2023
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    nums = []

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        self.nums = []
        self.dfs(root, '')
        result = sum(list(map(int, self.nums)))

        return result
    

    def dfs(self, node, num):
        num += str(node.val)
        if not node.left and not node.right:
            self.nums.append(num)
        
        if node.left:
            self.dfs(node.left, num)
        if node.right:
            self.dfs(node.right, num)