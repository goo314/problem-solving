"""LeetCode

Algorithm : 
    Dynamic Programming
Level :
    Medium
Status :
    Accepted

Sat Jan  4 15:44:50 KST 2025
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = -1

        dp = [0] + [-1] * amount
        for c in coins:
            if c <= amount:
                dp[c] = 1
        
        for i in range(1, amount+1):
            
            tmp = 1e9
            for c in coins:
                if 0 <= i-c and dp[i-c] != -1:
                    tmp = min(tmp, dp[i-c]+1)
            if tmp == 1e9:
                tmp = -1
            dp[i] = tmp
        
        result = dp[amount]
        return result

        """Better Answer
        dp = [amount+1] * (amount+1) # initialize with amount+1 (no need to set INF)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i-c < 0:
                    continue
                dp[i] = min(dp[i], dp[i-c]+1) # update dp everytime (clean code)
        
        if dp[amount] != amount+1: # reduce code comparing everytime in the loop
            result = dp[amount]
        """