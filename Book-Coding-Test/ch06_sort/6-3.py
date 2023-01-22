array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            print(array, i, j)
        else:
            break

print(array)

# Time complexity is: O(N^2)
# move current num to left until correct position
