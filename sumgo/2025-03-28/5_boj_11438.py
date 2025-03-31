import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

depth = [-1] * (n+1)
# visited = [False] * (n+1)
parent = [[0]*17 for _ in range(n+1)]

depth[1] = 0
s = [(1, 0)]
while s:
    cur, d = s.pop()
    # visited[cur] = True

    for nxt in adj[cur]:
        # if not visited[nxt]:
        if depth[nxt] == -1:
            depth[nxt] = d+1
            parent[nxt][0] = cur
            s.append((nxt, d+1))

for i in range(1, 17):
    for j in range(1, n+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

m = int(input())

ans = []
for _ in range(m):
    x, y = map(int, input().split())
    
    if depth[x] < depth[y]:
        x, y = y, x
    diff = depth[x] - depth[y]
    for i in range(17):
        if diff & (1 << i):
            x = parent[x][i]
    
    if x == y:
        # print(x)
        ans.append(str(x))
        continue
    
    for i in range(16, -1, -1):
        if parent[x][i] != parent[y][i]:
            x = parent[x][i]
            y = parent[y][i]
    
    # print(parent[x][0])
    ans.append(str(parent[x][0]))

print('\n'.join(ans))
