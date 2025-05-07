"""LeetCode

Algorithm : 
    Shortest Path
Level :
    Medium
Status :
    Accepted

Wed May  7 22:23:45 KST 2025
"""

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        
        from math import inf
        dist = [[inf]*m for _ in range(n)]
        
        import heapq
        pq = []
        heapq.heappush(pq, (0, (0, 0)))
        dist[0][0] = 0

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        ans = 0
        while pq:
            d, (x, y) = heapq.heappop(pq)
            if x == n-1 and y == m-1:
                ans = d
                break
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m:
                    nd = max(d+1, moveTime[nx][ny]+1)
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heapq.heappush(pq, (nd, (nx, ny)))

        return ans
