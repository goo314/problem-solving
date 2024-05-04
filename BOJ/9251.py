"""9251

Algorithm: 
    DP
Status:
    Pass
Tag:
    CJ올리브네트웍스
"""

import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

n, m = len(s1), len(s2)
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n-1][m-1])