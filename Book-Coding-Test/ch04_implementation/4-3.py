pos = input()
# it should be convenient when using ord " y = int(ord(pos[0])-int(ord('a')) "
column = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x, y = int(pos[1]), column.index(pos[0])

# I can initialize using tuple "dirs = [(-2, -1), (-1, -2), ...]"
dx = [-1,  1,  2,  2,  1, -1, -2, -2]
dy = [-2, -2, -1,  1,  2,  2,  1, -1]

count = 0
for i in range(8):
    # next position
    nx = x+dx[i]
    ny = y+dy[i]
    # is it possible?
    if 1<=nx and nx<=8 and 1<=ny and ny<=8:
        count += 1

print(count)
