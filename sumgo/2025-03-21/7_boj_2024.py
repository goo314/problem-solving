import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# init
s = 1 << (n-1).bit_length()
tree = [0] * (2*s)
for i in range(n):
    tree[s+i] = int(input())
for i in range(s-1, 0, -1):
    tree[i] = tree[2*i] + tree[2*i+1]

def query(l, r, i, query_l, query_r):
    if query_r < l or r < query_l:
        return 0
    if query_l <= l and r <= query_r:
        return tree[i]
    else:
        mid = (l+r)//2
        left = query(l, mid, 2*i, query_l, query_r)
        right = query(mid+1, r, 2*i+1, query_l, query_r)
        return left + right

def update(target, val):
    i = s+target-1
    tree[i] = val
    while i > 0:
        i //= 2
        tree[i] = tree[2*i] + tree[2*i+1]

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    elif a == 2:
        ans = query(1, s, 1, b, c)
        print(ans)