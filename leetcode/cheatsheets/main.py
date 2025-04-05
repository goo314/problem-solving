"""Cheat Sheet for Problem Solving
1. Arrays
2. Stack
3. Queue
4. Tree
5. Sorting
6. Graph
7. Minimum Spanning Tree
8. Disjoint Set
9. Dijkstra
10. Shortest Path
"""


def stack_fn():
    """Stack
    [1, 2, 3]
    
    Prints:
        3 2 1
    """
    s = []
    s.append(1)
    s.append(2)
    s.append(3)
    for _ in range(3):
        top = s.pop()
        print(top, end=' ')
    print()


def queue_fn():
    """Queue
    [1, 2, 3]

    Prints:
        1 2 3
    """
    from collections import deque
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    for _ in range(3):
        first = q.popleft()
        print(first, end=' ')
    print()


def heapq_fn():
    """Heap
        1
    2       3

    Prints:
        1 2 3
    """
    import heapq
    pq = []
    heapq.heappush(pq, 1)
    heapq.heappush(pq, 2)
    heapq.heappush(pq, 3)
    while pq:
        root = heapq.heappop(pq)
        print(root, end=' ')
    print()


def tree_fn():
    """Tree
        1
    2       3
    
    Prints:
        1
    """
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    print(root.val)


def binarysearch_fn():
    """Binary Search
    """
    pass


def countingsort_fn():
    """Counting Sort
    """
    pass


def bfs_fn(): # TODO: change to Graph ver.
    """BFS
              1
        2           3
    4       5   6       7

    Prints:
        1 2 3 4
    """
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    target = 4
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    from collections import deque
    q = deque([root])
    while q:
        cur = q.popleft()
        print(cur.val, end=' ')
        if cur.val == target:
            break
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    print()


def dfs_fn(): # TODO: change to Graph ver.
    """DFS
              1
        2           3
    4       5   6       7

    Prints:
        1 3 7 6 2 5 4
        Recursive DFS: 1 2 4 5 3 6 7
    """
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    target = 4
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    s = [root]
    while s:
        cur = s.pop()
        print(cur.val, end=' ')
        if cur.val == target:
            break
        if cur.left:
            s.append(cur.left)
        if cur.right:
            s.append(cur.right)
    print()
    
    # Recursive
    def dfs(cur, target):
        print(cur.val, end=' ')
        if cur.val == target:
            return
        if cur.left:
            dfs(cur.left, target)
        if cur.right:
            dfs(cur.right, target)
    print("Recursive DFS: ", end='')
    dfs(root, target)
    print()


def dijkstra_fn():
    """Dijkstra
    0 -(1)-> 1
     \       |
      \      |
       (3)  (1)
         \   |
          \  v
    2 <-(1)- 3

    Description:
        "한 정점에서 모든 정점까지의 최단 경로를 구하는 알고리즘"

    Prints:
        dist: [0, 1, 3, 2]
    """
    import heapq
    from math import inf
    start = 0
    graph = [
        [(1, 1), (3, 3)],
        [(3, 1)],
        [],
        [(2, 1)]
    ]

    dist = [inf]*4
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0
    while pq:
        d, v = heapq.heappop(pq)
        for nv, nw in graph[v]:
            nd = dist[v] + nw
            if nd < dist[nv]:
                dist[nv] = nd
                heapq.heappush(pq, (nd, nv))
    print("dist:", dist)


def disjointset_fn():
    """Disjoint Set
    0, 1
    2, 3, 4
    5

    Prints:
        parent: [0, 0, 2, 2, 5]
    """
    parent = [i for i in range(6)]

    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]
    def union(x, y):
        x, y = find_parent(x), find_parent(y)
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
    union(0, 1)
    union(2, 3)
    union(2, 4)
    print('parent:', parent)


def kruskal_fn():
    """Kruskal
     0 -(1)-- 1
     | \      |
     |  \     |
    (2)  (3) (1)
     |     \  |
     |      \ |
     2 --(1)- 3

    Description:
        Build the minimum spanning tree (=minimum cost to connect all points)
        모든 edge들을 순회하면서 cycle이 안 만들어지면 추가한다. 
    
    Explanation:
     0 -(1)-- 1
              |
              |
             (1)
              |
              |
     2 --(1)- 3

    Prints:
        3
    """
    parent = [i for i in range(4)]
    edges = [
        (1, 0, 1),
        (2, 0, 2),
        (3, 0, 3),
        (1, 1, 3),
        (1, 2, 3)
    ]

    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]
    def union(x, y):
        parent[find_parent(x)] = parent[find_parent(y)]
    
    edges.sort()
    ans = 0
    for w, u, v in edges:
        if find_parent(u) != find_parent(v):
            union(u, v)
            ans += w
    print(ans)


def prim_fn():
    """Prim
     0 -(1)-- 1
     | \      |
     |  \     |
    (2)  (3) (1)
     |     \  |
     |      \ |
     2 --(1)- 3

    Description:
        Build the minimum spanning tree (=minimum cost to connect all points)
        destination을 w와 같이 넣어서 작은 w로만 뻗어나간다. 
    
    Explanation:
     0 -(1)-- 1
              |
              |
             (1)
              |
              |
     2 --(1)- 3

    Prints:
        3
        parent: [0, 0, 3, 1]
    """
    edges = [
        (1, 0, 1),
        (2, 0, 2),
        (3, 0, 3),
        (1, 1, 3),
        (1, 2, 3)
    ]
    parent = [i for i in range(4)]
    visited = [False] * 4
    dist = [1e9] * 4

    from collections import defaultdict
    graph = defaultdict(list)
    for (w, u, v) in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    start = 0

    ans = 0
    import heapq
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        d, v = heapq.heappop(pq)
        if visited[v]:
            continue
        visited[v] = True
        ans += d
        for (u, w) in graph[v]:
            if not visited[u] and w < dist[u]:
                heapq.heappush(pq, (w, u))
                parent[u] = v
                dist[u] = w
                
    print(ans)
    print('parent:', parent)


def topological_fn():
    """Topological Algorithm
    0 -(1)-> 1
     \       |
      \      |
       (3)  (1)
         \   |
          \  v
    2 <-(1)- 3

    Prints:

    """
    edges = [
        (0, 1),
        (0, 3),
        (1, 3),
        (3, 2)
    ]

    from collections import defaultdict
    graph = defaultdict(list)

    indegree = [0] * 4
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    ans = []
    
    from collections import deque
    q = deque()

    for i in range(4):
        if indegree[i] == 0:
            q.append(i)

    while q:
        x = q.popleft()
        ans.append(x)
        for y in graph[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                q.append(y)
    print(ans)


def indexed_tree_fn(): # TODO: unfinish
    """Segmant Tree
               10(= 3+7)
        3(= 1+2)     7(= 3+4)
    1       2     3     4

    Description:


    """
    n = 4
    arr = [1, 2, 3, 4]

    s = 1
    while s < n:
        s *= 2
    
    tree = [0] * (2*s)

    # # Top-Down
    # def init(l, r, i):
    #     if l == r:
    #         tree[i] = arr[i-s]
    #     else:
    #         mid = (l+r)//2
    #         init(l, mid, 2*i)
    #         init(mid+1, r, 2*i+1)
    #         tree[i] = tree[2*i] + tree[2*i+1]

    # def query(l, r, i, query_l, query_r):
    #     if query_r < l or r < query_l:
    #         return 0
    #     elif query_l <= l and r <= query_r:
    #         return tree[i]
    #     else:
    #         mid = (l+r)//2
    #         left = query(l, mid, 2*i, query_l, query_r)
    #         right = query(mid+1, r, 2*i+1, query_l, query_r)
    #         return left+right

    # def update(l, r, i, target, diff):
    #     if target < l or r < target:
    #         return
    #     tree[i] += diff
    #     if l != r:
    #         mid = (l+r)//2
    #         update(l, mid, 2*i, target, diff)
    #         update(mid+1, r, 2*i+1, target, diff)
    
    # init(1, 4, 1)
    # print(tree)
    # print(query(1, s, 1, 1, 3))
    # update(1, s, 1, 3, -1)
    # print(tree)
    # print()
    
    # Bottom-Up
    def init():
        for i in range(2*s-1, 0, -1):
            if s <= i:
                tree[i] = arr[i-s]
            else:
                tree[i] = tree[2*i] + tree[2*i+1]
    
    def update(target, val):
        i = s+target-1
        tree[i] = val
        while True:
            i //= 2
            if i < 1:
                break
            tree[i] = tree[2*i] + tree[2*i+1]

    init()
    print(tree)
    update(2, 1)
    print(tree)
        

if __name__ == '__main__':    
    import sys
    import argparse

    functions = {
        'stack': stack_fn,
        'queue': queue_fn,
        'heapq': heapq_fn,
        'tree': tree_fn,
        'bfs': bfs_fn,
        'dfs': dfs_fn,
        'dijkstra': dijkstra_fn,
        'disjointset': disjointset_fn,
        'kruskal': kruskal_fn,
        'topological': topological_fn,
        'indexed_tree': indexed_tree_fn,
        'prim': prim_fn 
    }

    parser = argparse.ArgumentParser(description=f"Choose a function to run: {', '.join(functions.keys())}")
    parser.add_argument('function', choices=functions.keys(), help="Specify which function to run")
    args = parser.parse_args()
    functions[args.function]()
