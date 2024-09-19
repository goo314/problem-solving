"""LeetCode

Algorithm : 
    Dynamic Programming
Level :
    Easy
Status :
    Accepted

Sun Dec  3 14:49:25 PST 2023
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n+1):
            result.append(str(bin(i)).count('1'))

        return result