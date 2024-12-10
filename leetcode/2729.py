"""LeetCode

Algorithm : 
    Math
Level :
    Easy
Status :
    Accepted

Wed Dec 11 00:16:27 KST 2024
"""

class Solution:
    def isFascinating(self, n: int) -> bool:
        result = False

        s = str(n) + str(2*n) + str(3*n)
        if '0' in s:
            result = False
        elif len(s) == 9 and len(set(s)) == 9:
            result = True
        return result