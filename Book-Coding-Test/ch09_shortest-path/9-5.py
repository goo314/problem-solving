import sys
import heapq
input = sys.stdin.readline

n, m, c = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    edges[x].append((y, z)) # edges[v1] = (v2, w)

dist = [int(1e9)] * (n+1)

q = [] # (w, v)
heapq.heappush(q, (0, c))
dist[c] = 0

total_number = 0
total_time = 0

while q:
    w, v = heapq.heappop(q)
    if dist[v] < w:
        continue
    
    # total_number += 1
    # total_time = max(total_time, w)

    for nv, nw in edges[v]:
        if w + nw < dist[nv]:
            dist[nv] = w + nw
            heapq.heappush(q, (w+nw, nv))

for time in dist:
    if time < int(1e9):
        total_number += 1
        total_time = max(total_time, time)

print(total_number-1, total_time)