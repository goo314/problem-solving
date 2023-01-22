import sys
input = sys.stdin.readline

s = input()

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

count0 = 0 # from 1 to 0
count1 = 1 # from 0 to 1
if s[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count0 += 1
        else:
            count1 +=  1

# print(min(count0, count1))
