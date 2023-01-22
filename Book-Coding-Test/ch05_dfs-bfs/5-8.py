# dfs(adjacency matrix graph, currentNode, boolean list visited)
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# by principle of stack, it prints nodes reversely than what I thought
'''
def dfs(graph, v, visited):
    stack = []
    stack.append(v)

    # while stack is not empty
    while len(stack)>0:
        v = stack.pop()
        print(v, end = ' ')
        visited[v] = True

        # put adjacency node in stack
        for i in graph[pos]:
            if not visited[i]:
                stack.append(i)
'''

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
    ]

visited = [False]*9

dfs(graph, 1, visited)
