'''
1. 오름차순으로 정렬
2. 현재 그룹 current에 추가하면서 충분하면 다음 그룹으로 넘어가고 ret 값 1 증가
'''

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr = sorted(arr)

ret = 0
current = 0

for x in arr:
    current += 1
    if current >= x:
        ret += 1
        current = 0

print(ret)