"""Practices

Algorithm :
    Two Pointers
Level :
    Easy
"""
class Solution:
    # Fast and slow pointers
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 1
        while j < n:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1
