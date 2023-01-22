import sys
input = sys.stdin.readline

s = input()

ret = 0
for c in s:
    c = int(c)
    # 1*2 < 1+2, 값이 1이하인 경우에 곱셈보다 덧셈이 우선!
    if c <= 1 or ret <= 1:
        ret += c
    else:
        ret *= c

print(ret)