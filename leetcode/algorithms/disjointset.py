parent = []

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return x

def union_set(x, y):
    x, y = find_parent(x), find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y