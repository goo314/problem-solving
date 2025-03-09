class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        out = [0] * n
        reverse = [[] for _ in range(n)]

        for x in range(n):
            for y in graph[x]:
                reverse[y].append(x)
                out[x] += 1

        visited = [False] * n
        s = []
        for i in range(n):
            if out[i] == 0:
                s.append(i)

        ans = []
        while s:
            cur = s.pop()
            ans.append(cur)
            visited[cur] = True
            for next in reverse[cur]:
                out[next] -= 1
                if out[next] == 0 and not visited[next]:
                    s.append(next)
        
        ans.sort()
        return ans

