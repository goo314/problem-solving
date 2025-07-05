"""Practices

Algorithm :
    Greedy
Level :
    Medium
"""
class Solution:
    # Count overlapping intervals first
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        n = len(intervals)
        cnt = 1
        end = intervals[0][1]
        for x, y in intervals:
            if end <= x:
                cnt += 1
                end = y

        return n-cnt
