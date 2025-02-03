"""
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
    """BFS
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
        return x
    def union_set(x, y):
        x, y = find_parent(x), find_parent(y)
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
    union_set(0, 1)
    union_set(2, 3)
    union_set(2, 4)
    print('parent:', parent)


def kruskal_fn(): # TODO: wrong code
    """Kruskal
     0 -(1)-- 1
     | \      |
     |  \     |
    (2)  (3) (1)
     |     \  |
     |      \ |
     2 --(1)- 3

    Prints:
        5
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
        return x
    def union_set(x, y):
        x, y = find_parent(x), find_parent(y)
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
    
    edges.sort()
    result = 0
    for w, u, v in edges:
        if find_parent(u) != find_parent(v):
            union_set(u, v)
            result += w
    print(result)


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
        'kruskal': kruskal_fn
    }

    parser = argparse.ArgumentParser(description=f"Choose a function to run: {', '.join(functions.keys())}")
    parser.add_argument('function', choices=functions.keys(), help="Specify which function to run")
    args = parser.parse_args()
    functions[args.function]()