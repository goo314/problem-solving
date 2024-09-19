"""LeetCode

Algorithm : 
    DP
Level :
    Easy
Status :
    Accepted

Sun Dec  3 16:40:37 PST 2023
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = 0

        n = len(cost)
        dp = [1000]*n
        
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-2]+cost[i], dp[i-1]+cost[i])

        result = min(dp[n-2], dp[n-1])

        return result