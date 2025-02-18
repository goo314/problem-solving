"""LeetCode

Algorithm : 
    Stack
Level :
    Medium
Status :
    Accepted

Wed Feb 19 00:38:34 KST 2025
"""

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = ''

        n = len(pattern)
        s = []

        for i in range(n+1):
            s.append(str(i+1))
            if i == n or pattern[i] == 'I':
                while s:
                    ans += s.pop()
        return ans