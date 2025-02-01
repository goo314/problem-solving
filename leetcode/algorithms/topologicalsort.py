from collections import deque
n, m = map(int, input().split())
graph = []

indegree = [0] * n
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[x] += 1

result = []
q = deque()

for i in range(n):
    if indegree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    result.append(x)
    for y in graph[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            q.append(y)