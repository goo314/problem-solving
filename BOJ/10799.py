"""10799

Algorithm: 
    Stack
Status:
    Pass
Tag:
    CJ올리브네트웍스
"""

import sys
input = sys.stdin.readline

arr = input().rstrip()

result = 0

nums = 0
length = len(arr)

i = 0
while i < length:

    # Cut by laser
    if arr[i] == '(' and i+1<length and arr[i+1]==')':
        result += nums
        i += 1
    
    elif arr[i] == '(':
        nums += 1
    
    elif arr[i] == ')':
        result += 1
        nums -= 1
    
    i += 1

print(result)