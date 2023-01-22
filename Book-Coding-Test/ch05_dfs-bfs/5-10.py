def findIce(frame, n, m, x, y, visited):
    visited[x][y] = True

    # up down left right
    dx = [-1, 1,  0, 0]
    dy = [ 0, 0, -1, 1]

    # check adjacency node
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and frame[nx][ny]=='0':
                findIce(frame, n, m, nx, ny, visited)

n, m = map(int, input().split())
# could use [list(map(int, input())) for _ in range(n)] and it stores type int
frame = [input() for _ in range(n)]
visited = [[False]*m for _ in range(n)]

count = 0
for i in range(n):
    for j in range(m):
        if frame[i][j] == '0' and visited[i][j] == 0:
            findIce(frame, n, m, i, j, visited)
            count += 1

print(count)

'''
input is ...
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

it will print...
8
'''
