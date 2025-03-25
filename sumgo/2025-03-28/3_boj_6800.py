import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.char = ''
    def insert(self, char, bin):
        prev = self
        for i in range(len(bin)):
            b = bin[i]
            if b == '0' and prev.left:
                prev = prev.left
                continue
            elif b == '1' and prev.right:
                prev = prev.right
                continue
            
            cur = Node()
            if i == len(bin)-1:
                cur.char = char
            
            if b == '0':
                prev.left = cur
                prev = prev.left
            elif b == '1':
                prev.right = cur
                prev = prev.right

k = int(input())

root = Node()
for _ in range(k):
    c, bin = input().split()
    root.insert(c, bin)

ans = ''

seq = input().rstrip()

i = 0
while i < len(seq):
    cur = root
    while not cur.char:
        b = seq[i]
        if b == '0':
            cur = cur.left
        elif b == '1':
            cur = cur.right
        i += 1
    ans += cur.char
print(ans)
