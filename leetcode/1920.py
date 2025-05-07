"""LeetCode

Algorithm : 
    Array
Level :
    Easy
Status :
    Accepted

Wed May  7 22:33:55 KST 2025
"""

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
