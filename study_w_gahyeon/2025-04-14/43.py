def solution(s):
    ans = 0
    
    n = len(s)
    for i in range(n):
        tmp = s[i:] + s[:i]
        
        is_correct = True
        stack = []
        for c in tmp:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    is_correct = False
                    break
                if c == ')' and stack.pop() != '(':
                    is_correct = False
                    break
                if c == '}' and stack.pop() != '{':
                    is_correct = False
                    break
                if c == ']' and stack.pop() != '[':
                    is_correct = False
                    break
        if len(stack) != 0:
            is_correct = False
        
        if is_correct:
            ans += 1
    
    return ans
