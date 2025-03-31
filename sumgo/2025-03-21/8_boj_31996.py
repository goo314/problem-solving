# TODO
import sys
input = sys.stdin.readline

n, a = map(int, input().split())
string = '0' + input().rstrip()
cnt = list(string).count('1')

adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

# 1 0 1 1 0 1
#  -
#    -
#      -
#      ---
#      -----

visited = [False] * (n+1)
prev = [0] * (n+1)

s = [a]
end = a
while s:
    cur = s.pop()
    visited[cur] = True

    if string[cur] == '0':
        string[cur] = '1'
        cnt += 1
    else:
        string[cur] = '0'
        cnt -= 1
    
    if cnt == 0:
        end = cur
        break
    
    for nxt in adj[cur]:
        if not visited[nxt]:
            s.append(nxt)
            prev[nxt] = cur

ans = 0
... stack = 
while end != -1:
    stafk.24
    end = prev[end]
