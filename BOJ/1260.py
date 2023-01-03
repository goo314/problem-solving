import sys
from collections import deque
n, m, k = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def DFS(v, visited):
    visited[v] = True
    print(v, end = ' ')

    for nv in graph[v]:
        if not visited[nv]:
            visited[nv] = True
            DFS(nv, visited)

def BFS(v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        
        for nv in graph[v]:
            if not visited[nv]:
                visited[nv] = True
                queue.append(nv)

visited = [False]*(n+1)
DFS(k, visited)
print()
visited = [False]*(n+1)
BFS(k, visited)
