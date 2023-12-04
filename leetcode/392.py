"""LongestPanlindrome

Algorithm : 
    DP
Level :
    Easy
Status :
    Accepted

Sun Dec  3 17:03:13 PST 2023
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        result = False

        n = len(t)
        dp = [-1] * (n+1)

        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False

        dp[0] = 0 if s[0] == t[0] else -1
        for i in range(n):
            for j in range(i):
                if dp[j]+1 < len(s) and s[dp[j]+1] == t[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        if len(s)-1 in dp:
            result = True

        return result

        """
        result = False
        
        max = 0
        for x in t:
            if max < len(s) and x == s[max]:
                max += 1
        
        if max == len(s):
            result = True
        
        return result
        """