"""LeetCode

Algorithm : 
    Sort
Level :
    Medium
Status :
    Accepted

Thu Apr 24 00:34:13 KST 2025
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        ans = []

        n = len(intervals)
        s, e = intervals[0]
        for i in range(1, n):
            start, end = intervals[i]
            if e < start:
                ans.append([s, e])
                s, e = start, end
            else:
                e = max(e, end)
        ans.append([s, e])
        return ans
            
        
        print(ans)
