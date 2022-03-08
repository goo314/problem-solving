import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))

low, high = 0, max(trees)

height = 0
while low <= high:
    amount = 0
    mid = (low+high)//2
    for t in trees:
        if t > mid:
            amount += (t-mid)
    if amount < m:
        high = mid-1
    else:
        height = mid
        low = mid+1
print(height)
        
