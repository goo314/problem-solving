"""LeetCode

Algorithm : 
    Greedy
Level :
    Easy
Status :
    Accepted

Sun, Nov 26, 2023
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:

        upper = [0]*26
        lower = [0]*26

        for x in s:
            if x < 'a':
                upper[ord(x)-ord('A')] += 1
            else:
                lower[ord(x)-ord('a')] += 1
        
        letters = upper + lower

        result = 0
        odd = False
        for x in letters:
            result += (x//2)*2
            if x % 2 == 1:
                odd = True
        
        if odd:
            result += 1

        return result