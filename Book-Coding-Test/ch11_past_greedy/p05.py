import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = [0] * (m+1)
arr = list(map(int, input().split()))
for x in arr:
    num[x] += 1

ret = (n*(n-1))//2 # total case
for x in num:
    if x > 1:
        ret -= (x*(x-1))//2 # except the case when same weight

print(ret)