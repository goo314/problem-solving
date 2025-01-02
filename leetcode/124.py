"""LeetCode

Algorithm : 
    Tree
Level :
    Hard
Status :
    Accepted

Thu Jan  2 22:35:35 KST 2025
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = -1e9

    def traverse(self, cur: TreeNode):
        if cur is None:
            return 0

        left = max(0, self.traverse(cur.left))
        right = max(0, self.traverse(cur.right))

        self.result = max(self.result, left + right + cur.val)
        return max(left, right) + cur.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.result