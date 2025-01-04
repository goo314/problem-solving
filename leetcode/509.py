"""LeetCode

Algorithm : 
    DP
Level :
    Easy
Status :
    Accepted

Sun Dec  3 15:40:48 PST 2023
"""

class Solution:
    def fib(self, n: int) -> int:
        result = 0

        dp = [0]*(n+2)
        dp[0], dp[1] = 0, 1
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        result = dp[n]
        return result
    
    """Another Answer (with Recursion)
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0] * (n+1)
        return self.fibo(dp, n)

    def fibo(self, dp, n):
        if n == 1 or n == 2:
            return 1
        if dp[n] != 0:
            return dp[n]
        dp[n] = self.fibo(dp, n-1) + self.fibo(dp, n-2)
        return dp[n]
    """

    """Better Answer (with Space capacity O(1))
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        prev, cur = 1, 1
        for i in range(3, n+1):
            s = prev + cur
            prev = cur
            cur = s
        
        return cur
    """