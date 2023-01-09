import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    visit = [[False]*m for _ in range(n)]

    nodes = []

    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1
        nodes.append((x, y))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    ret = 0
    for node in nodes:
        q = []
        x, y = node[0], node[1]
        if visit[x][y]:
            continue

        ret += 1
        q.append((x, y))
        visit[x][y] = True
        while len(q)>0:
            x, y = q.pop(0)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if not visit[nx][ny] and arr[nx][ny]==1:
                    visit[nx][ny] = True
                    q.append((nx, ny))
    print(ret)