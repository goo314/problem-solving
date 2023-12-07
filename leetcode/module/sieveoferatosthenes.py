import math
n = int(input())
array = [True for i in range(n)]

for i in range(2, int(math.sqrt(n)+1)):
    if array[i]:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1