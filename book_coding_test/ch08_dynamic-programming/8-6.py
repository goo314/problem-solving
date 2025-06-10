n = int(input())
storage = list(map(int, input().split()))

d = [0]*100
d[0] = storage[0]
d[1] = max(storage[0], storage[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + storage[i])

print(d[n-1])
