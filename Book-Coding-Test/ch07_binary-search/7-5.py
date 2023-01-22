import sys

# Time complexity is O(NlogN) + O(MlogN) = O((N+M)logN)
# O(NlogN) for sorting items, O(MlogN) for find items
def binarySearch(array, target, start, end):
    if start > end:
        return -1
    mid = (start+end)//2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binarySearch(array, target, start, mid-1)
    else:
        return binarySearch(array, target, mid+1, end)

n = int(sys.stdin.readline().rstrip())
items = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
checkList = list(map(int, sys.stdin.readline().rstrip().split()))

items.sort()
for x in checkList:
    find = binarySearch(items, x, 0, n-1)
    if find == -1:
        print('no', end = ' ')
    else:
        print('yes', end = ' ')


# could use bucket sort
'''
count = [0]*1000001
for i in items:
    count[i] = 1
for x in checkList:
    if count[x] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
'''

# could use type set and it is the fastest
'''
items = set(map(int, input().split))
for x in checkList:
    if x in items:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
'''

'''
input is...
5
8 3 7 9 2
3
5 7 9

it will print...
no yes yes
'''
