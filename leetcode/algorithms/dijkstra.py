import heapq
INF = int(1e9)

n, m = map(int, input().split())
graph = [[]]

visited = [False] * (n+1)
dist = [INF] * (n+1)

pq = []
dist[start] = 0
heapq.heappush(pq, (0, start))

while pq:
    c, v = heapq.heappop(pq)
    visited[v] = True
    for nv, e in graph[v]:
        if not visited[nv] and dist[v] + w < dist[nv]:
            dist[nv] = dist[v] + w
            heapq.heappush(h, (dist[v] + w, nv))