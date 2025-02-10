"""LeetCode

Algorithm : 
    BFS
Level :
    Easy
Status :
    Accepted

Mon Feb 10 23:51:38 KST 2025
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        result = 0

        if not root:
            return result

        q = deque([(root, 1)])
        while q:
            cur, d = q.popleft()
            if not cur.left and not cur.right:
                result = d
                break
            if cur.left:
                q.append((cur.left, d+1))
            if cur.right:
                q.append((cur.right, d+1))

        return result