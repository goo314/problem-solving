"""LeetCode

Algorithm : 
    Dynamic Programming
Level :
    Medium
Status :
    Accepted

Tue May  6 00:35:18 KST 2025
"""

class Solution:
    def numTilings(self, n: int) -> int:
        
        dp = [0, 1, 2, 5]
        def tilings(n):
            if len(dp) > n:
                return dp[n]
            dp.append((tilings(n-1)*2+tilings(n-3))%(10**9+7))
            return dp[n]
        
        return tilings(n)
