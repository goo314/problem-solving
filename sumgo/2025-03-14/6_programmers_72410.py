def solution(new_id):
    answer = ''
    
    # 1
    answer = new_id.lower()
    
    # 2
    invalid = "~!@#$%^&*()=+[{]}:?,<>/"
    for c in invalid:
        answer = answer.replace(c, '')
    
    # 2
    while '..' in answer:
        answer = answer.replace("..", '.')
    
    # 4
    while answer and answer[0] == '.':
        answer = answer[1:]
    while answer and answer[-1] == '.':
        answer = answer[:-1]
        
    # 5
    if len(answer) == 0:
        answer = 'a'
    
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        while answer and answer[-1] == '.':
            answer = answer[:-1]
    
    # 7
    while len(answer) <= 2:
        answer += answer[-1]

    return answer