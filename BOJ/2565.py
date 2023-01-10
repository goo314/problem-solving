import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr = sorted(arr, key=lambda x: x[0])

dp = [0]*n
for i in range(n):
    a, b = arr[i]
    
    tmp = 0
    for j in range(i):
        if arr[j][1] < b and tmp < dp[j]:
            tmp = dp[j]
    dp[i] = tmp + 1

print(n-max(dp))