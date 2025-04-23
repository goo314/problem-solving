"""LeetCode

Algorithm : 
    Hash
Level :
    Easy
Status :
    Accepted

Thu Apr 24 00:16:08 KST 2025
"""

class Solution:
    def countLargestGroup(self, n: int) -> int:

        cnt = [0]*(n+1)

        for i in range(1, n+1):
            tmp = sum(list(map(int, list(str(i)))))
            cnt[tmp] += 1
        
        m = max(cnt)
        ans = cnt.count(m)
        return ans
