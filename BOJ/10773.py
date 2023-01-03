k = int(input())
stack = []

for _ in range(k):
    curNum = int(input())
    if curNum == 0:
        stack.pop()
    else:
        stack.append(curNum)

print(sum(stack))
