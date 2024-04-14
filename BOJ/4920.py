"""4920

Algorithm: 
    Brute Force
Status:
    Pass
Tag:
    CJ올리브네트웍스
"""

import sys
input = sys.stdin.readline

index = 1
while True:
    n = int(input())
    if n == 0:
        break
    arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

    result = -9e9
    for i in range(n):
        for j in range(n):
            # shape 1
            if j+3<n:
                area = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3]
                result = max(result, area)
            if i+3<n:
                area = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j]
                result = max(result, area)
            
            # shape 2
            if i+1<n and j+2<n:
                area = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2]
                result = max(result, area)
            if i+2<n and 0<=j-1:
                area = arr[i][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+2][j-1]
                result = max(result, area)
            
            # shape 3
            if i+1<n and j+2<n:
                area = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+2]
                result = max(result, area)
            if i+2<n and 0<=j-1:
                area = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j-1]
                result = max(result, area)
            if i+1<n and j+2<n:
                area = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
                result = max(result, area)
            if i+2<n and j+1<n:
                area = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+2][j]
                result = max(result, area)
            
            # shape 4
            if i+1<n and j+2<n:
                area = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]
                result = max(result, area)
            if i+2<n and 0<=j-1:
                area = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j-1]
                result = max(result, area)
            if i+1<n and 0<=j-1 and j+1<n:
                area = arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
                result = max(result, area)
            if i+2<n and j+1<n:
                area = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j+1] 
                result = max(result, area)
            
            # shape 5
            if i+1<n and j+1<n:
                area = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1]
                result = max(result, area)
    
    print(f'{index}. {result}')
    index += 1