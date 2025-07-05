"""Practices

Algorithm :
    Greedy
Level :
    Medium
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        tmp = 0
        for i in range(n):
            if tmp < i:
                return False
            tmp = max(i+nums[i], tmp)
        return True
