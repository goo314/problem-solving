from collections import deque

n, start, target = input(), input(), input()
graph = [[]]
visited = [False] * n

queue = deque([start])
while queue:
    # 1. get current
    v = queue.popleft()

    # 2. if is target
    if v == target:
        break

    # 3. for possible next hops
    for nv in graph[v]:
        # 4. if can go
        if not visited[nv]:
            # 5. check in
            visited[v] = True
            # 6. insert it to queue
            queue.append(nv)