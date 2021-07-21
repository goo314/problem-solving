eq = input()
precedureOP = {'+': 1, '-': 1, '*':2, '/':2, '(':0, ')':0} # precedure of operator

result = str()
stack = []
for s in eq:
    # if operand , attach to result
    if s not in precedureOP:
        result += s

    elif s == '(':
        stack.append(s)

    elif s == ')':
        while stack[-1] != '(':
            result += stack[-1]
            stack.pop()
        stack.pop()
    
    # if operator
    else:
        # at the top of stack , there always are op having low precedure
        while stack and precedureOP[stack[-1]] >= precedureOP[s]:
            result += stack[-1]
            stack.pop()
        stack.append(s)

# the rest part
while stack:
    result += stack[-1]
    stack.pop()

print(result)
