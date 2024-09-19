"""LeetCode

Algorithm : 
    Greedy
Level :
    Medium
Status :
    Accepted

Sun Nov 26 15:02:50 PST 2023
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        result = 0

        digits = list(map(int, list(n)))

        result = max(digits)

        return result