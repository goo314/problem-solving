'''
N = int(input())

ret = N // 500 ; N = N % 500
ret += N // 100 ; N = N % 100
ret += N // 50 ; N = N % 50
ret += N // 10 ; N = N % 10

print(ret)
'''

'''
coin = [500, 100, 50, 10]
ret = 0

for i in range(4):
    if N == 0:
        break
    ret += N // coin[i]
    N = N % coin[i]

print(ret)
'''

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n//coin
    n %= coin

print(count)
