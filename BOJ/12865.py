import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [-1]*(k+1)
dp[0] = 0

ret = 0
for _ in range(n):
    w, v = map(int, input().split())
    
    for i in range(k, 0, -1):
        if i-w < 0:
            break
        if dp[i-w] == -1:
            continue
        if dp[i] < dp[i-w]+v:
            dp[i] = dp[i-w]+v
        if ret < dp[i]:
            ret = dp[i]

print(ret)