import sys
input = sys.stdin.readline

def countCompanies(friends_nodes, friends_from, friends_to, friends_weight):
    num_weight = max(friends_weight)

    # friends_edges[c][v1] = v2
    friends_edges = [[[] for _ in range(friends_nodes)] for _ in range(num_weight)]
    friends_visited = [[False] * friends_nodes for _ in range(num_weight)]
    
    # initialize
    n = len(friends_from)
    for i in range(n):
        v1 = friends_from[i] - 1
        v2 = friends_to[i] - 1
        c = friends_weight[i] - 1
        friends_edges[c][v1].append(v2)
        friends_edges[c][v2].append(v1)

    ret = 0
    for c in range(num_weight):
        edges = friends_edges[c]
        visited = friends_visited[c]

        while False in visited:
            v1 = visited.index(False)
            
            q = []
            q.append(v1)
            visited[v1] = True

            group = []
            
            # proceed bfs
            while len(q) > 0:
                v1 = q[0]
                q.pop(0)
                group.append(v1)
                
                for v2 in edges[v1]:
                    if not visited[v2]:
                        q.append(v2)
                        visited[v2] = True

            group = sorted(group, key=lambda x: -x)
            if len(group) >= 2:
                temp = (group[0]+1)*(group[1]+1)
                if ret < temp:
                    ret = temp
            
    return ret

friends_nodes = int(input())
n = int(input())
friends_from = [int(input()) for _ in range(n)]
n = int(input())
friends_to = [int(input()) for _ in range(n)]
n = int(input())
friends_weight = [int(input()) for _ in range(n)]

print(countCompanies(friends_nodes, friends_from, friends_to, friends_weight))