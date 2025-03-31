"""
dic = dict()
adj = [[] for _ in range(n)]

for i in range(n):
    tmp = list(map(int, input().split()))
    dic[i] = tmp[0]
    adj[i] = [x-1 for x in tmp[1:-1]]

print(dic)
print(adj)

for i in range(n):
    ans = 0
    for j in adj[i]:
        ans += dic[j]
    ans += dic[i]
    print(ans)
"""

import sys
input = sys.stdin.readline

n = int(input())
indegree = [0] * (n+1)
adj = [[] for _ in range(n+1)]
time = [0] * (n+1)
ans = [0] * (n+1)

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    time[i] = tmp[0]
    for j in tmp[1:-1]:
        adj[j].append(i)
    indegree[i] = len(tmp[1:-1])

from collections import deque
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        ans[i] = time[i]

while q:
    cur = q.popleft()
    
    for nxt in adj[cur]:
        indegree[nxt] -= 1

        ans[nxt] = max( ans[nxt], ans[cur] + time[nxt] )
        
        if indegree[nxt] == 0:
            q.append(nxt)

for a in ans[1:]:
    print(a)