# Recursive version
def binarySearch(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif target < array[mid]:
        return binarySearch(array, target, start, mid-1)
    else:
        return binarySearch(array, target, mid+1, end)

# Loop version
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid-1
        else:
            start = mid+1
    return None

n, target = 10, 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# result = binarySearch(array, target, 0, n-1)
result = binary_search(array, target, 0, n-1)
if result == None:
    print('None')
else:
    print(result + 1)

# Only for sorted array
# Time complexity is O(logN)
