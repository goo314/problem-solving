n, k = map(int, input().split())

count = 0

# maybe it returns 'time out'
'''
while n!= 1:
    if n%k == 0:
        n /= k
    else:
        n -= 1
    count += 1
'''

# maybe it runs only when n is k^x+r (x is integer)
'''
r = n % k
count += r
n -= r

while n!= 1:
    n /= k
    count += 1
'''

# wrong since n in while loop might not be divided by k
'''
r = n % k
count += r
n -= r

while n >= k:
    n //= k
    count += 1

count += n-1
'''

while True:
    # use 1st operation to make multiple of k
    count += n % k
    n -= n % k
    # don't need 2nd operation if n is smaller than k
    if n < k:
        break
    # use 2nd operation
    n //= k
    count += 1

count += n-1

print(count)

