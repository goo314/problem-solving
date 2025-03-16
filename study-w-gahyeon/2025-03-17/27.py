def solution(strings, n):
    answer = []
    
    answer = sorted(strings)
    answer = sorted(answer, key= lambda x:x[n])
    
    return answer