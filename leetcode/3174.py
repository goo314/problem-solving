"""LeetCode

Algorithm : 
    Stack
Level :
    Easy
Status :
    Accepted

Tue Feb 11 00:20:23 KST 2025
"""

class Solution:
    def clearDigits(self, s: str) -> str:
        print(ord('a'), ord('0'), ord('9'))
        
        i, result = 0, str(s)
        while True:
            n = len(result)
            if i >= n:
                break
            if ord('0') <= ord(result[i]) <= ord('9'):
                result = result[:i-1] + result[i+1:]
                i -= 1
            else:
                i += 1
        return result