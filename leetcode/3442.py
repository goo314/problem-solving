"""LeetCode

Algorithm : 
    Hash
Level :
    Easy
Status :
    Accepted

Tue Jun 10 23:37:38 KST 2025
"""

class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = [0]*26
        for c in s:
            cnt[ord(c)-ord('a')] += 1
        
        even, odd = len(s), 0
        for x in cnt:
            if x!=0 and x%2 == 0:
                even = min(even, x)
            else:
                odd = max(odd, x)
        
        ans = odd - even
        return ans
