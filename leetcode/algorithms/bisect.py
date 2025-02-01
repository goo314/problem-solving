from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

left = bisect_left(a, x) # 2
right = bisect_right(a, x) # 4

# count the number of values in [x, y]
def count_by_range(array, x, y):
    right = bisect_right(array, y)
    left = bisect_left(array, x)
    return right - left

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
count = count_by_range(array, 4, 4) # 2
count = count_by_range(array, -1, 3) # 6