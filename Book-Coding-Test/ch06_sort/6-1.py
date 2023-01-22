array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

'''
for i in range(len(array)):
    m = i
    for j in range(i+1, len(array)):
        if array[j] < array[m]:
            m = j
    array[i], array[m] = array[m], array[i]
'''

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# Time complexity is : N+N-1+N-2+...+2 = O(N^2)
# find minimum after index i and swap
