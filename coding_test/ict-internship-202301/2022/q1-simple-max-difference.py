import sys
input = sys.stdin.readline

n = int(input())
px = [int(input()) for _ in range(n)]

m = 10**5+1
ret = -1

for p in px:
    ret = max(ret, p-m)
    m = min(m, p)
print(ret)