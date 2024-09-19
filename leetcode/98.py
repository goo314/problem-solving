"""LeetCode

Algorithm : 
    DFS
Level :
    Medium
Status :
    Failed

Mon Nov 27 22:55:36 PST 2023
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        result = self.isBST(root)

        return result

    def isBST(self, node):
        if not node.left and not node.right:
            return True
        elif not node.left:
            return node.val < node.right.val
        elif not node.right:
            return node.left.val < node.val
        
        # Every left subnodes are less than root node and right subnodes too.
        if self.isBST(node.left) and self.isBST(node.right) and node.left.val < node.val and node.val < node.right.val:
            return True
        else:
            return False

    """Answer

    result = isBST(root, float("-inf"), float("inf"))

    def isBST(self, node, min, max):
        if not node:
            return True
        
        if node.val <= min or node.val >= max:
            return False
        
        return self.isBST(node.left, min, node.val) and self.isBST(node.right, node.val, max)    
    

    """