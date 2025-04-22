"""LeetCode

Algorithm : 
    Dynamic Programming
Level :
    Medium
Status :
    Accepted

Wed Apr 23 01:07:19 KST 2025
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        
        n = len(prices)
        for i in range(1, n):
            ans += max(prices[i]-prices[i-1], 0)
        
        return ans
