class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 1. check row
        for i in range(9):
            cnt = [0] * 10
            for x in board[i]:
                if x != ".":
                    if cnt[int(x)] > 0:
                        return False
                    cnt[int(x)] += 1

        # 2. check column
        for j in range(9):
            cnt = [0] * 10
            for i in range(9):
                x = board[i][j]
                if x != ".":
                    if cnt[int(x)] > 0:
                        return False
                    cnt[int(x)] += 1

        # 3. check sub-boxes
        for i in range(3):
            for j in range(3):
                cnt = [0] * 10
                for r in range(3*i, 3*i+3):
                    for c in range(3*j, 3*j+3):
                        x = board[r][c]
                        if x != ".":
                            if cnt[int(x)] > 0:
                                return False
                            cnt[int(x)] += 1
        
        return True
