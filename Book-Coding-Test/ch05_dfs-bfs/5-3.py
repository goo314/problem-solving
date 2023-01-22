def recursive_func(n):
    if(n == 0):
        return
    print('this is recursive function')
    recursive_func(n-1)

recursive_func(5)

def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

print(factorial(3))
