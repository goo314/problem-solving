"""LeetCode

Algorithm : 
    Stack
Level :
    Medium
Status :
    Accepted

Tue Feb 11 23:54:40 KST 2025
"""

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n, m = len(s), len(part)

        i = 0
        while i < n:
            if s[i:i+m] == part:
                s = s[:i] + s[i+m:]
                n, i = len(s), i-m
                continue
            i += 1
        return s

        """Better Answer
        - use stack and compare top elements with part
        """