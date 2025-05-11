"""LeetCode

Algorithm : 
    Prefix Sum
Level :
    Hard
Status :
    Accepted

Sun May 11 14:43:01 KST 2025
"""

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        from collections import defaultdict
        n, m = len(grid), len(grid[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        d = defaultdict(list)

        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+grid[i-1][j-1]
                d[grid[i-1][j-1]].append((i, j))
        
        # horizontal
        for i in range(1, n):
            tmp, rest = dp[i][-1], dp[-1][-1]-dp[i][-1]
            is_equal = False
            if tmp == rest:
                return True
            if tmp>rest:
                if i == 1:
                    if tmp-rest in [grid[i-1][0],grid[i-1][-1]]:
                        return True
                else:
                    for j, k in d[tmp-rest]:
                        if j>i:
                            continue
                        if m == 1 and j!=1 and j!=i:
                            continue
                        is_equal = True
                        break
            else:
                if i == n-1:
                    if rest-tmp in [grid[i][0],grid[i][-1]]:
                        return True
                else:
                    for j, k in d[rest-tmp]:
                        if j<=i:
                            continue
                        if m == 1 and j!=i and j!=n:
                            continue
                        is_equal = True
                        break
            if is_equal:
                return True
    
        # vertical
        for i in range(1, m):
            tmp, rest = dp[-1][i], dp[-1][-1]-dp[-1][i]
            is_equal = False
            if tmp == rest:
                return True
            if tmp>rest:
                if i == 1:
                    if tmp-rest in [grid[0][i-1],grid[-1][i-1]]:
                        return True
                else:
                    for k, j in d[tmp-rest]:
                        if j>i:
                            continue
                        if m == 1 and j!=1 and j!=i:
                            continue
                        is_equal = True
                        break
            else:
                if i == n-1:
                    if rest-tmp in [grid[0][i],grid[-1][i]]:
                        return True
                else:
                    for k, j in d[rest-tmp]:
                        if j<=i:
                            continue
                        if m == 1 and j!=i and j!=m:
                            continue
                        is_equal = True
                        break
            if is_equal:
                return True
        
        return False

"""
Note: 
    Failed during weekly contest.
"""
