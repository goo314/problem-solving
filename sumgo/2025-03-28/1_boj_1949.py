# TODO
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n = int(input())
arr = [0] + list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n+1)
dp_check = [0] * (n+1)
dp_nocheck = [0] * (n+1)

def dfs(cur):
    visited[cur] = True
    
    dp_check[cur] = arr[cur]
    dp_nocheck[cur] = 0
    
    for nxt in adj[cur]:
        if not visited[nxt]:
            dfs(nxt)
            dp_nocheck[cur] += max(dp_check[nxt], dp_nocheck[nxt])
            dp_check[cur] += dp_nocheck[nxt]

dfs(1)
ans = max(dp_check[1], dp_nocheck[1])
print(ans)
        
