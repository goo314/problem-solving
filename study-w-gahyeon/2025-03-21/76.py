def solution(command):
    ans = [0, 0]
    
    # up, right, down, left
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    dir = 0
    for c in command:
        if c == 'R':
            dir += 1
            dir %= 4
        elif c == 'L':
            dir -= 1
            dir %= 4
        elif c == 'G':
            ans = [ans[0]+dx[dir], ans[1]+dy[dir]]
        else:
            ans = [ans[0]-dx[dir], ans[1]-dy[dir]]
    
    return ans