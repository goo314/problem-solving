def solution(my_string):
    answer = ''
    
    d = dict()
    for c in my_string:
        if c in d:
            continue
        answer += c
        d[c] = True
    
    return answer
