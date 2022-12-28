import sys
# more faster than using input()
m = int(sys.stdin.readline())
s = set()

for _ in range(m):
    # use rstrip to remove enter char
    info = sys.stdin.readline().rstrip().split()
    
    if info[0] == 'add':
        s.add(int(info[1]))

    elif info[0] == 'remove':
        if int(info[1]) in s:
            s.remove(int(info[1]))

    elif info[0] == 'check':
        if int(info[1]) in s:
            print(1)
        else:
            print(0)

    elif info[0] == 'toggle':
        if int(info[1]) in s:
            s.remove(int(info[1]))
        else:
            s.add(int(info[1]))    

    elif info[0] == 'all':
        s = {i for i in range(1, 21)}

    # when info[0] is 'empty'
    else:
        s = set()

'''
input is...
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1

it will print...
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
'''
