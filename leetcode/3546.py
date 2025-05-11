"""LeetCode

Algorithm : 
    Prefix Sum
Level :
    Medium
Status :
    Accepted

Sun May 11 14:45:26 KST 2025
"""

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        hor = [sum(row) for row in grid]
        ver = []
        for j in range(m):
            tmp = 0
            for i in range(n):
                tmp += grid[i][j]
            ver.append(tmp)
        
        total = sum(hor)
        
        tmp = 0
        for h in hor:
            tmp += h
            if tmp == total-tmp:
                return True
        tmp = 0
        for v in ver:
            tmp += v
            if tmp == total-tmp:
                return True
        
        return False
