# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        arr = []
        s = [root]
        while s:
            cur = s.pop()
            arr.append(cur.val)
            if cur.left:
                s.append(cur.left)
            if cur.right:
                s.append(cur.right)
        
        arr.sort()
        
        result = 1e6
        n = len(arr)
        for i in range(1, n):
            diff = arr[i]-arr[i-1]
            result = min(result, diff)
        return result