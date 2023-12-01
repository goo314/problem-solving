array = []

def binarysearch(array, target, start, end):
    if start > end:
        return None
    
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif target < array[mid]:
        return binarysearch(array, target, start, mid-1)
    else:
        return binarysearch(array, target, mid+1, end)

binarysearch(array, target, 0, len(array)-1)

def binarysearch2(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

binarysearch(array, target, 0, len(array)-1)