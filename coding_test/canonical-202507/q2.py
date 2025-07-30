from typing import List


def solve(incoming: int) -> List[int]:
    ans = []

    n = abs(incoming)
    is_prime = [True]*(n+1)
    
    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]:
            continue

        for j in range(i*i, n, i):
            is_prime[j] = False

        while n%i == 0:
            n //= i
            ans.append(i)
    
    if n != 1:
        ans.append(n)
    if incoming < 0:
        ans[0] = -ans[0]
    return ans

inputs = [-190, -191, 192, -193, -194, 195, 196, 197, 198, 199]
for input in inputs:
    print(solve(input))

