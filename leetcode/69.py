"""LeetCode

Algorithm : 
    Binary Search
Level :
    Easy
Status :
    Accepted

Sat Dec  2 17:38:07 PST 2023
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0

        start, end = 1, x
        while start <= end:
            mid =(start+end)//2
            result2, mid2 = result**2, mid**2
            if mid2 == x:
                result = mid
                break
            
            if 0 < x-mid2 < x-result2:
                result = mid
            
            if mid2 < x:
                start = mid + 1
            if x < mid2:
                end = mid - 1

        return result