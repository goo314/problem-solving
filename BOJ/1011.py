import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    dist = y - x
    if dist == 1:
        print(1)
        continue
    
    ret, var = 0, 1
    while 2*var <= dist:
        dist -= 2*var
        ret, var = ret+2, var+1
    
    while dist > 0:
        dist -= var
        ret, var = ret+1, var-1

    print(ret)
