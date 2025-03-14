import sys
input = sys.stdin.readline

nv, ne = map(int, input().split())
graph = [[] for _ in range(nv+1)]
for _ in range(ne):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(x):
    dist = [1e9] * (nv+1)
    import heapq
    pq = []
    heapq.heappush(pq, (0, x))
    dist[x] = 0

    while pq:
        d, u = heapq.heappop(pq)
        for v, w in graph[u]:
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist

v1to = dijkstra(v1)
v2to = dijkstra(v2)

if 1e9 in (v1to[1], v1to[v2], v2to[nv]) and 1e9 in (v2to[1], v2to[v1], v1to[nv]):
    print(-1)
elif 1e9 in (v1to[1], v1to[v2], v2to[nv]):
    print(v2to[1] + v2to[v1] + v1to[nv])
elif 1e9 in (v2to[1], v2to[v1], v1to[nv]):
    print(v1to[1] + v1to[v2] + v2to[nv])
else:
    print(min(v2to[1] + v2to[v1] + v1to[nv], v1to[1] + v1to[v2] + v2to[nv]))