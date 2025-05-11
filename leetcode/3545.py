"""LeetCode

Algorithm : 
    Hash
Level :
    Easy
Status :
    Accepted

Sun May 11 14:44:51 KST 2025
"""

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        
        
        d = dict()
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        cnt = len(list(d.keys()))
        if cnt < k:
            return 0
        
        tmp = list(d.values())
        tmp.sort()
        
        ans = 0
        diff = cnt - k
        ans = sum(tmp[:diff])
        return ans
