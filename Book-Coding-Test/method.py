import sys
input = sys.stdin.readline

# priority queue 
# heapq가 일반적으로 더 빠르게 동작
import heapq
q = []
x = 1
heapq.heappush(q, x)
x = heapq.heappop(q)