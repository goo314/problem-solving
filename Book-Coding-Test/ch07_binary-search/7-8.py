import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
riceCakes = list(map(int, sys.stdin.readline().rstrip().split()))

# Time out ( I guess that time complexity is O(NlogN)+O(2billion-M) )
'''
riceCakes.sort(reverse = True)
h = riceCakes[0]
i = 0 # location of it which is taller than h
amount = 0

while amount < m:
    h -= 1
    while riceCakes[i+1] > h:
        i += 1
    amount += i+1

print(h)
'''

# Parametric Search
start = 0
end = max(riceCakes)

result = 0
while (start <= end):
    total = 0
    mid = (start+end)//2
    for x in riceCakes:
        if x > mid:
            total += x-mid
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)

'''
input is...
4 6
19 15 10 17

it will print...
15
'''
