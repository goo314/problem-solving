"""
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

s = int(n**(1/2))
n_d = (n+s-1)//s
d = [1e9] * n_d

# init
for i in range(n):
    idx = i // s
    d[idx] = min(d[idx], arr[i])

def query(l, r, val):
    ans = 0

    for i in range(l, min(r+1, (l//s + 1) * s)):
        if val < arr[i]:
            ans += 1
    
    for i in range(max(l, (r//s) * s), r+1):
        if val < arr[i]:
            ans += 1
    
    for i in range(l//s+1, r//s):
        if d[i] <= val:
            for j in range(i*s, i*s+s):
                if j < n and val < arr[j]:
                    ans += 1
    
    return ans
    
def update(target, val):
    arr[target] = val
    
    idx = target // s
    d[idx] = 1e9
    for i in range(idx*s, idx*s+s):
        if i < n:
            d[idx] = min(d[idx], arr[i])

m = int(input())
for _ in range(m):
    print(d)
    q = list(map(int, input().split()))
    if q[0] == 1:
        print(query(q[1]-1, q[2]-1, q[3]))
    elif q[0] == 2:
        update(q[1]-1, q[2])
"""

import sys
import math
import bisect

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

s = int(math.sqrt(n))
block_count = (n + s - 1) // s
blocks = [[] for _ in range(block_count)]

for i in range(n):
    blocks[i // s].append(arr[i])
for i in range(block_count):
    blocks[i].sort()

def query(l, r, x):
    ans = 0

    while l <= r and l % s != 0:
        if arr[l] > x:
            ans += 1
        l += 1

    while l <= r and r % s != s - 1:
        if arr[r] > x:
            ans += 1
        r -= 1

    while l <= r:
        block_idx = l // s
        ans += len(blocks[block_idx]) - bisect.bisect_right(blocks[block_idx], x)
        l += s

    return ans

def update(i, y):
    block_idx = i // s
    old_value = arr[i]
    arr[i] = y

    idx = bisect.bisect_left(blocks[block_idx], old_value)
    if idx < len(blocks[block_idx]) and blocks[block_idx][idx] == old_value:
        blocks[block_idx].pop(idx)

    bisect.insort(blocks[block_idx], y)

m = int(input())
for _ in range(m):
    q = list(map(int, input().split()))
    if q[0] == 1:
        print(query(q[1]-1, q[2]-1, q[3]))
    elif q[0] == 2:
        update(q[1]-1, q[2])






s = int(math.sqrt(n))
block_count = (n + s - 1) // s
blocks = [[] for _ in range(block_count)]

for i in range(n):
    blocks[i // s].append(arr[i])
for i in range(block_count):
    blocks[i].sort()

def query(l, r, val):
    ans = 0
    for i in range(l//s, r):
        if i % s == 0:
            break
        if arr[i] > val:
            ans += 1
    
    for i in range(r//s, l, -1):
        if r%s == 0:
            break
        if arr[i] > val:
            ans += 1
    
    import bisect
    for i in range(l//s, r//s):
        ans += s - bisect.bisect_right(blocks[i], val)
    
    return ans


def update(target, val):
    blocks[target//s].remove(target%s)
    blocks[target//s].append(val)
    blocks[target//s].sort()