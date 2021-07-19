from collections import deque

def modifiedBFS(maze, n, m):
    queue = deque([(0, 0)])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y]+1

    return maze[n-1][m-1]

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
print(modifiedBFS(maze, n, m))

'''
input is ...
4 6
101111
101010
101011
111011

it will print...
15
'''
