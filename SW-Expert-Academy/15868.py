import sys

t = int(sys.stdin.readline().rstrip())

for x in range(1, t+1):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    
    first = sys.stdin.readline().rstrip()

    ret = 'yes'
    
    for _ in range(1, n):
        arr = sys.stdin.readline().rstrip()
        
        a = int(first[0])
        
        if bool(int(arr[0])):
            b = int(not a)
        else:
            b = a

        for i in range(1, m):
            a = int(first[i])

            if b ^ a != int(arr[i]):
                ret = 'no'
                break
    
    print('#'+str(x), ret)