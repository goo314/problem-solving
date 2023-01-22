import time
# Time complexity is THETA(1,618...^N)
def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-2) + fibo(n-1)

startTime = time.time()
print(fibo(30))
endTime = time.time()
print('fibo :', endTime-startTime)
print()

# Memoization is to store memory in order not to calculate same one twice or more
# Time complexity is O(N)
# Top-Down is... from the top to the bottom
d = [0]*100 # DP table
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    if d[n]!=0:
        return d[n]
    d[n] = fibonacci(n-1) + fibonacci(n-2)
    return d[n]

startTime = time.time()
print(fibonacci(99))
endTime = time.time()
print('fibonacci using memoization(top-down) :', endTime-startTime)
print()

# Bottom-Up is... from the bottom to the top
startTime = time.time()
d[1] = 1
d[2] = 1
n = 99
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])
endTime = time.time()
print('fibonacci using memoization(bottom-up) :', endTime-startTime)
