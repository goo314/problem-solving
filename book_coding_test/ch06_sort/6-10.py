n = int(input())
arr = [int(input()) for _ in range(n)]

# Bubble sort
'''
for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
'''

# Selection sort
'''
for i in range(len(arr)):
    max_index = i
    for j in range(i, len(arr)):
        if arr[j] > arr[max_index]:
            max_index = j
    arr[i], arr[max_index] = arr[max_index], arr[i]
'''

# Insertion sort
'''
for i in range(len(arr)-1):
    for j in range(i, 0, -1):
        if arr[j-1] < arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
'''

# Quick sort
'''
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    arrNoPivot = arr[1:]
    left = [x for x in arrNoPivot if x>=pivot]
    right = [x for x in arrNoPivot if x<pivot]
    return quickSort(left) + [pivot] + quickSort(right)
arr = quickSort(arr)
'''


arr = sorted(arr, reverse=True)

for x in arr:
    print(x, end = ' ')

'''
input is...
3
15
27
12

it will print...
27 15 12
'''
