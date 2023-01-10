import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0]*(k+1)
data = []
for _ in range(n):
    x = int(input())
    data.append(x)

dp[0] = 1
for x in data:
    for i in range(x, k+1):
        dp[i] += dp[i-x]

print(dp[k])