import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

"""시간초과
class Node:
    def __init__(self, val, d):
        self.val = val
        self.depth = d
        self.parent = None

from collections import deque
q = deque()
root = Node(1, 0)
q.append(root)
nodes = [None, root] + [None]*n

while q:
    cur = q.popleft()
    for nxt in adj[cur.val]:
        if not nodes[nxt]:
            next = Node(nxt, cur.depth+1)
            next.parent = cur
            nodes[nxt] = next
            q.append(next)

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    node_x, node_y = nodes[x], nodes[y]
    while node_x != node_y:
        if node_x.depth < node_y.depth:
            node_y = node_y.parent
        elif node_x.depth > node_y.depth:
            node_x = node_x.parent
        else:
            node_x = node_x.parent
            node_y = node_y.parent

    print(node_x.val)
"""

depth = [0] * (n+1)
visited = [False] * (n+1)
parent = [[0]*17 for _ in range(n+1)]

s = [(1, 0)]
while s:
    cur, d = s.pop()
    visited[cur] = True
    depth[cur] = d

    for nxt in adj[cur]:
        if not visited[nxt]:
            parent[nxt][0] = cur
            s.append((nxt, d+1))

for i in range(1, 17):
    for j in range(1, n+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    
    if depth[x] < depth[y]:
        x, y = y, x
    diff = depth[x] - depth[y]
    for i in range(16, -1, -1):
        if diff & (1 << i):
            x = parent[x][i]

    ans = x    
    if x != y:
        for i in range(16, -1, -1):
            if parent[x][i] != parent[y][i]:
                x = parent[x][i]
                y = parent[y][i]
        ans = parent[x][0]
    
    print(ans)