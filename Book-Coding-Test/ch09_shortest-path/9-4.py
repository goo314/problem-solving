import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dist = [[int(1e9)]*n for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    dist[v1-1][v2-1] = 1
    dist[v2-1][v1-1] = 1

for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

x, k = map(int, input().split())

ret = dist[1][k-1]+dist[k-1][x-1]
if ret >= int(1e9):
    print(-1)
else:
    print(ret)

