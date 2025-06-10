array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')

# Time complexity is: O(N+K), where K is max(array)
# Inconvinient memory
# Proper when there are many repetitions of numbers
