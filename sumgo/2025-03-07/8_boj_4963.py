while True:
    w, h = map(int, input().split())
    
    if w == h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]

    dx = [-1, 1, 0, -1]
    dy = [0, 1, -1, 1]
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                s = [(i, j)]
                while s:
                    x, y = s.pop()
                    for i in range(4):
                        nx, ny