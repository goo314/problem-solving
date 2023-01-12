import sys
input = sys.stdin.readline

s = input().rstrip()

ret = 0
cur = s[0]
for bit in s:
    if cur != bit:
        ret += 1
        cur = bit

if ret%2 == 1:
    ret = ret//2 + 1
else:
    ret = ret//2

print(ret)