"""Practices

Algorithm :
    Two Pointers
Level :
    Medium
"""
class Solution:
    def longestPalindrome(self, s: str) -> str: 
        n = len(s)
        ans = s[0]
        for i in range(n):
            for j in range(i+2, n+1):
                tmp = s[i:j]
                if len(ans)<j-i and tmp == tmp[::-1]:
                    ans = tmp
        return ans

class Solution2:
    # Expand around center -> Time: O(N^2)
    # Check both odd-length and even-length palindrome
    def longestPalindrome(self, s: str) -> str: 
        n = len(s)

        def longest(l, r):
            while 0<=l and r<n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        ans = s[0]
        for i in range(n):
            s1 = longest(i, i)
            s2 = longest(i, i+1)
            if len(ans) < len(s1):
                ans = s1
            if len(ans) < len(s2):
                ans = s2
        
        return ans
