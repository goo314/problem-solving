
'''
1, 2, 3일 경우 1부터 1+2+3까지의 수를 다 만들 수 있다.
1, 2, 3, 5일 경우 6=1+2+3>5, 1+2+3+5까지의 수를 다 만들 수 있다.
1, 2, 3, 5, 13일 경우 11=1+2+3+5<13, 12를 만들 수 없다.
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

target = 1
for x in arr:
    if target < x:
        break
    target += x

print(target)