array = []

count = [0] * (max(array)+1)

for x in array:
    count[x] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)