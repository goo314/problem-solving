# TODO
import sys
input = sys.stdin.readline

n, a = map(int, input().split())
s = input().rstrip()

adj = [[] for _ in range(n)]
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