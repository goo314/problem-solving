array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# General quick sort algorithm
def quickSort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left<=end and array[left]<=array[pivot]:
            left += 1
        while right>start and array[right]>=array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quickSort(array, start, right-1)
    quickSort(array, right+1, end)

quickSort(array, 0, len(array)-1)
print('quickSort', array)

# Python version
def quick_sort(array):
    if len(array)<=1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print('quick_sort', quick_sort(array))

# Python version2
def QuickSort(array):
    if len(array) > 1:
        pivot = array[-1]
        left, mid, right = [], [], []

        for i in range(len(array)-1):
            if array[i] < pivot:
                left.append(array[i])
            elif array[i] > pivot:
                right.append(array[i])
            else:
                mid.append(array[i])
        mid.append(pivot)

        return QuickSort(left)+mid+QuickSort(right)
    
    else:
        return array

print('QuickSort', QuickSort(array))

# Time complexity is: O(NlogN)
