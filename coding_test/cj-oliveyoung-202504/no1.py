# This is not the actual solution used during the exam.

import heapq

def solution(m, v):
    pq = []
    
    for i in range(m):
        heapq.heappush(pq, (0, i))

    n = len(v)
    for coin in v:
        c, idx = heapq.heappop(pq)
        heapq.heappush(pq, (c+coin, idx))
    
    return heapq.heappop(pq)[0]
    
    
# 가짜 테스트케이스
m = 3
v = [1, 2, 3]
print(1 == solution(m, v))

m = 4
v = [1, 10, 2, 20, 1, 30]
print(2 == solution(m, v))
