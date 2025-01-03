"""LeetCode

Algorithm : 
    Prefix Sum
Level :
    Medium
Status :
    Accepted

Fri Jan  3 23:58:06 KST 2025
"""

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        result = 0

        n = len(nums)
        dp = [0] * (n-1)
        reverse_dp = [0] * (n-1)

        dp[0] = nums[0]
        for i in range(1, n-1):
            dp[i] = dp[i-1] + nums[i]
        
        reverse_dp[n-2] = nums[n-1]
        for i in range(n-3, -1, -1):
            reverse_dp[i] = reverse_dp[i+1] + nums[i+1]
        
        for i in range(n-1):
            if dp[i] >= reverse_dp[i]:
                result += 1
        return result

        """Better Answer
        result = 0
        left, right = 0, sum(nums)

        n = len(nums)
        for i in range(n-1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                result += 1
        return result
        """