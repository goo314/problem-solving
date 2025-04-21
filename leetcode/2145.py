"""LeetCode

Algorithm : 
    Prefix Sum
Level :
    Medium
Status :
    Accepted

Mon Apr 21 23:46:23 KST 2025
"""

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        n = len(differences)
        tmp = [lower]
        for d in differences:
            tmp.append(tmp[-1]+d)
        
        low, up= min(tmp), max(tmp)
        ans = max((upper-up) - (lower-low) + 1, 0)
        return ans
