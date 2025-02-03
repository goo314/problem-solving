"""LeetCode

Algorithm : 
    Array
Level :
    Easy
Status :
    Accepted

Mon Feb  3 22:07:20 KST 2025
"""

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        result = 0

        n = len(nums)
        if n == 0:
            return 0
        
        inc, dec = 1, 1
        tmp_inc, tmp_dec = 1, 1
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                tmp_inc += 1
                tmp_dec = 1
            elif nums[i-1] > nums[i]:
                tmp_inc = 1
                tmp_dec += 1
            else:
                tmp_inc = 1
                tmp_dec = 1
            inc = max(inc, tmp_inc)
            dec = max(dec, tmp_dec)
        
        result = max(inc, dec)
        return result