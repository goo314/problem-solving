"""1654

Algorithm: 
    Parametric Search
Status:
    Pass
Tag:
    CJ올리브네트웍스
"""

import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
arr = [int(input()) for _ in range(k)]

_max = sum(arr) // n
_min = 1

def howmany(arr, l):
    ret = 0
    for x in arr:
        ret += x // l
    return ret

while _min <= _max:
    mid = (_min + _max) // 2
    num = howmany(arr, mid)
    if num < n:
        _max = mid - 1
    else:
        _min = mid + 1

print(_max)