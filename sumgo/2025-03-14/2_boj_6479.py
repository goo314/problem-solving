import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    
    edges = [list(map(int, input().split())) for _ in range(n)]

    parent = [i for i in range(m)]
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union(x, y):
        parent[find_parent(x)] = parent[find_parent(y)]

    edges.sort(key=lambda x: x[2])

    ans = 0
    for (x, y, z) in edges:
        if find_parent(x) != find_parent(y):
            union(x, y)
        else:
            ans += z

    print(ans)