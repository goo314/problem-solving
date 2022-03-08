def findVillage(x, y, graph, n, visited, count):
    visited[x][y] = True
    count+= 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if graph[nx][ny] == 1 and not visited[nx][ny]:
            count = findVillage(nx, ny, graph, n, visited, count)

    return count

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

numOfHouse = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            numOfHouse.append(findVillage(i, j, graph, n, visited, 0))

numOfHouse.sort()
print(len(numOfHouse))
for x in numOfHouse:
    print(x)
