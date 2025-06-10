n, k = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA = sorted(arrA)
arrB = sorted(arrB, reverse = True)

# Wrong since it performs when arrA[i]<arrB[i] and it's not the answer
'''
for i in range(k):
    arrA[i] = arrB[i]
'''

for i in range(k):
    if arrA[i] < arrB[i]:
        arrA[i], arrB[i] = arrB[i], arrA[i]
    else:
        break

print(sum(arrA))

'''
input is...
5 3
1 2 5 4 3
5 5 6 6 5

it will print...
26
'''
