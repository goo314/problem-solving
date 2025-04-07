import sys
input = sys.stdin.readline

n, q = map(int, input().split())
tastes = list(map(int, input().split()))
sizes = list(map(int, input().split()))
d = dict()
for i in range(n):
    t, s = tastes[i], sizes[i]
    if t in d:
        size, cnt = d[t]
        if s < size:
            continue
        elif s == size:
            d[t] = (s, cnt+1)
        else:
            d[t] = (s, 1)    
    else:
        d[t] = (s, 1)

tmp = sorted(list(d.keys()), reverse=True)
for i in range(1, len(tmp)):
    ta, tb = tmp[i], tmp[i-1]
    size_a, cnt_a = d[ta]
    size_b, cnt_b = d[tb]
    if size_a < size_b:
        d[ta] = size_b, cnt_b
    elif size_a == size_b:
        d[ta] = size_a, cnt_a + cnt_b

import bisect
keys = sorted(d.keys())
for _ in range(q):
    p = int(input())
    i = bisect.bisect_left(keys, p)
    if i == len(keys):
        print(0)
    else:
        print(d[keys[i]][1])
