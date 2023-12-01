# O(NlgN)
array = []

def quicksort(array, start, end):
    if start >= end:
        return
    pivot = start
    left, right = start+1, end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quicksort(array, start, right-1)
    quicksort(array, right+1, end)

quicksort(array, 0, len(array)-1)


def quicksort2(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    arr = array[1:]

    left = [x for x in arr if x <= pivot]
    right = [x for x in arr if x > pivot]

    return quicksort2(left)+[pivot]+quicksort2(right)