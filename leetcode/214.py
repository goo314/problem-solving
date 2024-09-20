"""LeetCode

Algorithm : 
    String Matching
Level :
    Hard
Status :
    Accepted

Sat Sep 21 01:20:33 KST 2024
"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:

        result = ''

        n = len(s)
        reverse_s = s[::-1]

        for i in range(n):
            if s[:n-i] == reverse_s[i:]:
                result = reverse_s + s[n-i:]
                break

        return result