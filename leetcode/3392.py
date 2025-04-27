"""LeetCode

Algorithm : 
    Array
Level :
    Easy
Status :
    Accepted

Sun Apr 27 21:34:56 KST 2025
"""

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(0, n-2):
            if nums[i+1] == 2*(nums[i]+nums[i+2]):
                ans += 1
        
        return ans
