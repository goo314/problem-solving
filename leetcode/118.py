"""LeetCode

Algorithm : 
    DP
Level :
    Easy
Status :
    Accepted

Sun Dec  3 15:29:42 PST 2023
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]*(i+1) for i in range(numRows)]

        for i in range(2, numRows):
            for j in range(1, i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]

        return result