n = int(input())
peoples = list(map(int, input().split()))
peoples.sort()

print(peoples)

result = 0
for i in range(n):
    result += sum(peoples[:i+1])
print(result)

'''
input is...
5
3 1 4 3 2

it will print...
32
'''
