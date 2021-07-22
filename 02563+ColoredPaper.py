import sys
n = int(sys.stdin.readline().rstrip())
plane = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    # place where colored paper exist in is 1
    for i in range(x, x+10):
        for j in range(y, y+10):
            plane[i][j] = 1

area = 0
for i in range(100):
    area += plane[i].count(1)

print(area)


'''
input is...
3
3 7
15 7
5 2

it will print...
260
'''
