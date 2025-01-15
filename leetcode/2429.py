"""LeetCode

Algorithm : 
    Greedy
Level :
    Medium
Status :
    Accepted

Wed Jan 15 22:49:27 KST 2025
"""

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = 0

        k = str(bin(num2)).count('1')
        
        num1 = list(str(bin(num1)))[2:]
        n = len(num1)

        i = n-1
        while i >= 0 and k > 0:
            if num1[n-1-i] == '1':
                result += 2**i
                k -= 1
            i -= 1
        
        i = 0
        while k > 0:
            if i < n and num1[n-1-i] == '1':
                i += 1
                continue
            result += 2**i
            i += 1
            k -= 1
        
        return result