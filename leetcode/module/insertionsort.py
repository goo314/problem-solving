# O(N^2)
array = []

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        # swap until find the correct position
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break