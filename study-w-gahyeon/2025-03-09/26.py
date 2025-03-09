def solution(s):
    answer = ''
    
    s = list(s)
    s.sort(reverse=True)
    answer = ''.join(s)
    
    return answer