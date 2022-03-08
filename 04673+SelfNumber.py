def d(n):
    ret = n
    while n > 0:
        ret += n%10
        n //= 10
    return ret

whole = {i for i in range(1, 10001)}
nonSelf = set()
for i in range(10001):
    nonSelf.add(d(i))

answer = list(whole - nonSelf)
answer.sort()
for i in range(len(answer)):
    print(answer[i])
