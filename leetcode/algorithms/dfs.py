n, target = input(), input()
graph = [[]]
visited = [False] * n

def dfs(v):
    # 1. check in
    visited[v] = True

    # 2. if is target
    if v == target:
        return

    # 3. for possible next hops
    for nv in graph[v]:
        # 4. if can go
        if not visited[nv]:
            # 5. go
            dfs(nv)