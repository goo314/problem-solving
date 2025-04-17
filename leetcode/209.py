"""LeetCode

Algorithm : 
    Binary Search
Level :
    Medium
Status :
    Accepted

Fri Apr 18 01:52:28 KST 2025
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        if target in nums:
            return 1
        
        if sum(nums) < target:
            return 0

        dp = [0] * n
        ans = n

        for i in range(n):
            dp[i] = dp[i-1] + nums[i] if i>0 else nums[i]
            if dp[i] >= target:
                ans = min(ans, i+1)
        
        for i in range(n-1, -1, -1):
            l, r = 0, i-1
            while l <= r:
                mid = (l+r)//2
                if dp[i]-dp[mid] >= target:
                    ans = min(ans, abs(i-mid))
                    l = mid+1
                else:
                    r = mid-1
        return ans
