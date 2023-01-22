n = int(input())

arr = list()
for _ in range(n):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))

arr = sorted(arr, key = lambda x:x[1])
for student in arr:
    print(student[0], end = ' ')

'''
input is...
홍길동 95
이순신 77

it will print...
이순신 홍길동
'''
