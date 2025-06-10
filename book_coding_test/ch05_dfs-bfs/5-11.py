from collections import deque

def modifiedBFS(maze, n, m, visited):
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        # could use another simple condition , if nx<0 or nx>n: continue
        if y+1<m:
            # check maze[x][y]==1 to determine not visit and no evil
            if not visited[x][y+1] and maze[x][y+1]!=0:
                queue.append((x, y+1))
                visited[x][y+1] = True
                maze[x][y+1] = maze[x][y]+1
        if x+1<n:
            if not visited[x+1][y] and maze[x+1][y]!=0:
                queue.append((x+1, y))
                visited[x+1][y] = True
                maze[x+1][y] = maze[x][y]+1

    return maze[n-1][m-1]

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
print(modifiedBFS(maze, n, m, visited))

'''
input is ...
5 6
101010
111111
000001
111111
111111

it will print...
10
'''
