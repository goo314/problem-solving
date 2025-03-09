def solution(citations):
    answer = 0
    
    citations.sort()
    
    n = len(citations)
    for i in range(n):
        h = citations[i]
        if h >= n-i:
            return n-i
        # if n-i >= h:
        #     answer = h
        # else:
        #     answer = max(answer, n-i)
    
    return answer