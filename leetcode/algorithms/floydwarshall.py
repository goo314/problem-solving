n, m = map(int, input().split())
dist = [[INF]*n for _ in range(n)]

for _ in range(m):
    a, b= map(int, input().split())
    dist[a][b] = c

for i in range(n):
    dist[i][j] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])