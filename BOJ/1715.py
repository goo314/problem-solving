import sys
import heapq
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]

q = []
for x in data:
    heapq.heappush(q, x)

ret = 0
while len(q) > 1:
    subsum = heapq.heappop(q) + heapq.heappop(q)
    heapq.heappush(q, subsum)
    ret += subsum

print(ret)