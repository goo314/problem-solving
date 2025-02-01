from disjointset import find_parent, union_set

edges = [(c, a, b)]
edges.sort()

result = 0
for w, x, y in edges:
    if find_parent(x) != find_parent(y):
        union_set(x, y)
        result += w