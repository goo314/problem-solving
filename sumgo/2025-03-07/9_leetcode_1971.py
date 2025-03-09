class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        parent = [i for i in range(n)]

        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]

        for (u, v) in edges:
            parent_u, parent_v = find_parent(u), find_parent(v)
            if parent_u < parent_v:
                parent[parent_u] = parent_v
            else:
                parent[parent_v] = parent_u
        
        return find_parent(source) == find_parent(destination)