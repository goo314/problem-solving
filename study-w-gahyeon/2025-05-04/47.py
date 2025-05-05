def solution(n, results):
    
    graph = [[0]*(n+1) for _ in range(n+1)]
    for (a, b) in results:
        graph[a][b] = 1
        graph[b][a] = -1
        
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if graph[i][j] == graph[j][k] == 1:
                    graph[i][k] = 1
                    graph[k][i] = -1
                elif graph[i][j] == graph[j][k] == -1:
                    graph[i][k] = -1
                    graph[k][i] = 1
    
    ans = 0
    for g in graph:
        if g.count(0) == 2:
            ans += 1
    
    return ans
