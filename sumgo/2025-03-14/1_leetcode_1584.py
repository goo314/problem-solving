class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)

        import heapq
        pq = []
        
        # edges = []
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = abs(x1-x2) + abs(y1-y2)
                # edges.append((d, i, j))
                heapq.heappush(pq, (d, i, j))

        parent = [i for i in range(n)]

        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]

        def union(u, v):
            parent[find_parent(u)] = parent[find_parent(v)]
        

        ans = 0
        # edges.sort()
        # for (d, u, v) in edges:
        #     if find_parent(u) != find_parent(v):
        #         union(u, v)
        #         ans += d
       
        while pq:
            d, u, v = heapq.heappop(pq)
            if find_parent(u) != find_parent(v):
                union(u, v)
                ans += d
        
        return ans

        