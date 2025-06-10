n, m = map(int, input().split())
a, b, d = map(int, input().split())
world = list()
for _ in range(n):
    world.append( list(map(int, input().split())) )

visit = [[0]*m for _ in range(n)]

# (0 for north) -> (1 for left) -> (2 for south) -> (3 for right)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

count = 1
while True:
    move = False
    visit[a][b] = 1
    for i in range(1, 5):
        t = (d+i)%4
        na = a+dx[t]
        nb = b+dy[t]
        if 0<=na<n and 0<=nb<n:
            if visit[na][nb] == 0 and world[na][nb]==0:
                a, b, d = na, nb, t
                count += 1
                move = True
                break

    # if there's no path
    if move == False:
        # check backward
        ba = a+dx[(d+2)%4]
        bb = a+dy[(d+2)%4]
        if world[ba][bb] == 0:
            a, b = ba, bb
        # there's sea and break the loop
        else:
            break
print(count)
