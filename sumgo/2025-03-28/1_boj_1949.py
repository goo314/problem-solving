# TODO
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

ans = 0

        
