"""Practices

Algorithm :
    DFS
Level :
    Medium
"""
class Solution:
    # Mark non-surrounded regions with # 
    # Remove inner(surrounded) regions
    # Restore # regions to O
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def dfs(x, y, mark):
            if x<0 or x>=n or y<0 or y>=m:
                return
            if board[x][y] != 'O':
                return
            
            board[x][y] = mark
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                dfs(nx, ny, mark)
        
        for i in range(n):
            dfs(i, 0, '#')
            dfs(i, m-1, '#')
        
        for j in range(m):
            dfs(0, j, '#')
            dfs(n-1, j, '#')

        for i in range(1, n):
            for j in range(1, m-1):
                dfs(i, j, 'X')
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == '#':
                    board[i][j] = 'O'

