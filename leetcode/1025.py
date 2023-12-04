"""LongestPanlindrome

Algorithm : 
    DP
Level :
    Easy
Status :
    Accepted

Sun Dec  3 16:23:04 PST 2023
"""

class Solution:
    def divisorGame(self, n: int) -> bool:
        result = False

        dp = [n+1] * (n+1)
        dp[0] = 0

        for i in range(n+1):
            for j in range(1, n-i):
                if (n-i) % j == 0:
                    dp[i+j] = min(dp[i+j], dp[i]+1)
        
        # unintended but got answer
        if dp[n-1] <= n and dp[n]%2 == 1:
            result = True

        return result

    """
    return not n % 2
    """