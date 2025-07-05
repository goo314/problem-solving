"""Practices

Algorithm :
    Binary Search
Level :
    Medium
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r)//2
            tmp = 0
            for x in piles:
                tmp += x//mid
                if x%mid:
                    tmp += 1
            
            if tmp <= h:
                r = mid-1
            else:
                l = mid+1
        
        return l
