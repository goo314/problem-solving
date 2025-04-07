class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n

        dp[0] = nums[0]
        for i in range(1, n):
            num = nums[i]
            if dp[i-1] < 0:
                dp[i] = num
            else:
                dp[i] = dp[i-1] + num
        
        return max(dp)
