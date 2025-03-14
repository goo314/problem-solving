import sys
input = sys.stdin.readline

nv, ne = map(int, input().split())
graph = [[] for _ in range(nv)]

k = int(input())-1
for _ in range(ne):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))

dist = [1e9]*nv

import heapq
pq = []
heapq.heappush(pq, (0, k))
dist[k] = 0

while pq:
    d, v = heapq.heappop(pq)
    for (nv, nw) in graph[v]:
        nd = dist[v] + nw
        if nd < dist[nv]:
            dist[nv] = nd
            heapq.heappush(pq, (nd, nv))


for d in dist:
    if d == 1e9:
        print('INF')
    else:
        print(d)