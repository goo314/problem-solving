import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

s = 1
while s < n:
    s *= 2

tree = [0]*(2*s)
def init():
    for i in range(2*s-1, 0, -1):
        if s <= i:
            tree[i] = arr[i-s]
        else:
            tree[i] = tree[2*i] + tree[2*i+1]

def update(target, val):
    i = s+target-1
    tree[i] = val
    while True:
        i //= 2
        if i < 1:
            break
        tree[i] = tree[2*i] + tree[2*i+1]

def query(l, r, i, query_l, query_r):
    if query_r < l or r < query_l:
        return 0
    elif query_l <= l and r <= query_r:
        return tree[i]
    else:
        mid = (l+r)//2
        left = query(l, mid, 2*i, query_l, query_r)
        right = query(mid+1, r, 2*i+1, query_l, query_r)
        return left + right

init()

for _ in range(m):
    query = input()
    if query[0] == '1':
        i, j, k = map(int, query[1:].split())
    else:
        i, k = map(int, query[1:].split())
        