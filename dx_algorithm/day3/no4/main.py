import sys
# input = sys.stdin.readline

sys.stdin = open("input.txt", "r")

t = 10
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    cmds = list(input().split())
    pos = 0
    
    for i in range(m):
        cmd = cmds[pos:]
        if cmd[0] == 'I':
            x, y = int(cmd[1]), int(cmd[2])
            s = list(map(int, cmd[3:3+y]))
            pos += 3+y
            for j in range(y):
                arr.insert(x+j, s[j])
        elif cmd[0] == 'D':
            x, y = map(int, cmd[1:3])
            pos += 3
            del arr[x:x+y]
        elif cmd[0] == 'A':
            y = int(cmd[1])
            s = list(map(int, cmd[2:2+y]))
            pos += 2+y
            for j in range(y):
                arr.append(s[j])
    
    print("#"+str(tc), end=" ")
    for i in range(10):
        print(arr[i], end=" ")
    print()