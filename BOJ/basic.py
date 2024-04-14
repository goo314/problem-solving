"""basic
Tag:
    CJ올리브네트웍스
"""

"""Input

rstrip := remove enter
x, y = map(int, input().rstrip().split())

"""
import sys
input = sys.stdin.readline
# n, m, k = map(int, input().split())
# print(n, m, k)

"""비트연산
AND: &
OR: |
XOR: ^
NOT: ~
*2: << 
/2: >>
"""
a, b = 1, 0
# print(a&b)

"""Linked List
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

head = Node(0)
head.next = Node(1)
head.next.next = Node(2)

# cur = head
# while cur is not None:
#     print(cur.val, end=" ")
#     cur = cur.next
# print()

"""Tree
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def size(self):
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        return left_size + right_size + 1
    
    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1

root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.right.right = Node(3)
# print(root.depth())

"""BFS
"""
from collections import deque

# n, start, target = input(), input(), input()
# graph = [[]]
# visited = [False] * n

# queue = deque([start])
# while queue:
#     v = queue.popleft()

#     if v == target:
#         break

#     for nv in graph[v]:
#         if not visited[nv]:
#             visited[v] = True
#             queue.append(nv)

"""DFS
"""
# n, target = input(), input()
# graph = [[]]
# visited = [False] * n

# def dfs(v):
#     visited[v] = True

#     if v == target:
#         return

#     for nv in graph[v]:
#         if not visited[nv]:
#             dfs(nv)

"""Heap
priority queue 
heapq가 일반적으로 더 빠르게 동작
"""
import heapq
q = []
heapq.heappush(q, 1)
heapq.heappush(q, 4)
heapq.heappush(q, 2)
while q:
    print(heapq.heappop(q), end=' ') # 1 2 4
print()