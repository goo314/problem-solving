"""LongestPanlindrome

Algorithm : 
    BFS
Level :
    Easy
Status :
    Accepted

Mon Nov 27 23:47:25 PST 2023
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = self.isSame(p, q)

        return result
    
    def isSame(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        
        if node1.val != node2.val:
            return False
        
        left = self.isSame(node1.left, node2.left)
        right = self.isSame(node1.right, node2.right)

        return left and right