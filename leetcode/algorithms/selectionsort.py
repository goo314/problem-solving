# O(N^2)
array = []

for i in range(len(array)):
    # find minimum
    min = i
    for j in range(i+1, len(array)):
        if array[j] < min:
            min = array[j]
    # swap
    array[i], array[j] = array[min], array[i]