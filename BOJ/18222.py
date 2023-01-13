import sys
input = sys.stdin.readline

""" 
Thue-Morse Sequence
    t(0) = 0
    t(2n) = t(n)
    t(2n+1) = 1-t(n)
"""

def thue_morse(n):
    if n == 0:
        return "0"
    elif n%2 == 0:
        return thue_morse(n//2)
    else:
        return str(1-int(thue_morse(n//2)))

k = int(input())

print(thue_morse(k-1))