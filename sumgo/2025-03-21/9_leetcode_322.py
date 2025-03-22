class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] + [amount+1] * amount
        
        for i in range(amount+1):
            for c in coins:
                if i == c:
                    dp[i] = 1
                elif i-c > 0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        
        if dp[amount] == amount+1:
            return -1
        return dp[amount]
