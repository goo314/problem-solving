"""LeetCode

Algorithm : 
    Hash
Level :
    Medium
Status :
    Accepted

Mon May 12 23:49:37 KST 2025
"""

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        
        ans = 0
        for answer in answers:
            if answer == 0:
                ans += 1
                continue
            cnt[answer] += 1
            if cnt[answer] == answer+1:
                ans += answer+1
                cnt[answer]=0
        
        for k, v in list(cnt.items()):
            if v>0:
                ans += k+1

        return ans
