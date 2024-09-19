"""LeetCode

Algorithm : 
    BFS
Level :
    Medium
Status :
    Accepted

Mon Nov 27 23:54:35 PST 2023
"""

from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        result = True

        visited = [False] * len(rooms)

        queue = deque()

        start = 0
        queue.append(start)
        visited[start] = True

        while queue:
            x = queue.popleft()
            for nx in rooms[x]:
                if not visited[nx]:
                    visited[nx] = True
                    queue.append(nx)
        
        if False in visited:
            result = False

        return result