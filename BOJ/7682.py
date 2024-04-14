"""7682

Algorithm: 
    
Status:
    Failed
Tag:
    CJ올리브네트웍스
"""
import sys
input = sys.stdin.readline

while True:
    board = input().rstrip()
    
    if board == "end":
        break
    
    x = board.count('X')
    o = board.count('O')
    if abs(x-o) > 1:
        print("invalid")
        continue

    if '.' in board:
        if (board[0] == board[1] == board[2]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8]):
            print("valid")
        elif (board[0] == board[3] == board[6]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]):
            print("valid")
        elif (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]):
            print("valid")
        else:
            print("invalid")
        continue
        
    print("none")