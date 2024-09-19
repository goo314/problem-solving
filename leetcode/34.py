"""LeetCode

Algorithm : 
    Binary Search
Level :
    Medium
Status :
    Accepted

Sat Dec  2 17:52:35 PST 2023
"""

from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []

        left = bisect_left(nums, target)
        right = bisect_right(nums, target)

        if left == right:
            result = [-1, -1]
        else:
            result = [left, right-1]

        return result