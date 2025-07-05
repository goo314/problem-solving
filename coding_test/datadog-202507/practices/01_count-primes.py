"""Practices

Algorithm :
    Number Theory
Level :
    Medium
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True] * n
        
        i = 2
        while i*i < n:
            if not is_prime[i]:
                i += 1
                continue
            for j in range(i*2, n, i):
                is_prime[j] = False
            i += 1
        
        return max(is_prime.count(True)-2, 0)

class Solution2:
    # Start j from i*i
    def countPrimes(self, n: int) -> int:
        is_prime = [True] * n

        for i in range(2, int(n**0.5)+1):
            if not is_prime[i]:
                continue
            
            for j in range(i*i, n, i):
                is_prime[j] = False
                
        return max(is_prime.count(True)-2, 0)
