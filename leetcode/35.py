"""LeetCode

Algorithm : 
    Binary Search
Level :
    Easy
Status :
    Accepted

Thu Nov 30 23:21:54 PST 2023
"""

from bisect import bisect_left, bisect_right
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result = 0
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        result = (left+right)//2
        
        return result