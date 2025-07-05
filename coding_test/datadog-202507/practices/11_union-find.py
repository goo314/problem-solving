"""Practices

Algorithm :
    Disjoint Set
Note:
    sets: (0, 1), (2, 3, 4), (5)
    parent: [0, 0, 2, 2, 2, 5]
"""
parent = [i for i in range(6)]

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]
        
def union(x, y):
    x, y = find_parent(x), find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
union(0, 1)
union(2, 3)
union(2, 4)
print('parent:', parent)
