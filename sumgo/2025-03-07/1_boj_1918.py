inorder = input()

n = len(inorder)
ps = []
ops = []

OP = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

ans = ""
i = 0

while i < n:
    cur = inorder[i]
    
    if cur == ')':
        while ops:
            p_cur = ops.pop()
            if p_cur == '(':
                break
            ans += p_cur
    
    elif cur == '(':
        ops.append(cur)

    elif cur in OP:
        while ops and OP[cur] <= OP[ops[-1]]:
            ans += ops.pop()
        ops.append(cur)

    else:
        ans += cur
    
    i += 1

while ops:
    ans += ops.pop()
print(ans)
