"""LeetCode

Algorithm : 
    Array
Level :
    Medium
Status :
    Accepted

Wed May  7 22:52:40 KST 2025
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        n = len(nums)
        dp = [n+1]*n
        dp[0] = 0

        for i in range(n):
            num = nums[i]
            for j in range(i, i+num+1):
                if j >= n:
                    break
                dp[j] = min(dp[j], dp[i]+1)
        
        return dp[n-1]
        """
        
        n = len(nums)
        ans = 0
        tmp, end = 0, 0
        for i in range(n-1):
            end = max(end, i+nums[i])
            if i == tmp:
                ans += 1
                tmp = end
        return ans
