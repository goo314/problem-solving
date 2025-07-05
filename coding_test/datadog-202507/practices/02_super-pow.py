"""Practices

Algorithm :
    Divide and Conquer
Level :
    Medium
"""
class Solution:
    # Modular arithmetic: (a*b) % k = ((a%k)*(b%k)) % k
    # Law of exponents: a**(10*n+m) = (a**m) *((a**n)**10)
    def superPow(self, a: int, b: List[int]) -> int:
        
        def pow(a, k):
            if k < 10:
                return (a**k)%1337
            if k%2 == 0:
                return (pow(a, k//2) * pow(a, k//2))%1337
            return (pow(a, k-1) * (a%1337))%1337
        
        def superpow(a, b):
            if not b:
                return 1
            tmp1 = pow(a, b[-1])
            tmp2 = pow(superpow(a, b[:-1]), 10)
            return (tmp1*tmp2) % 1337
        
        return superpow(a, b)
        