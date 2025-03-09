def solution(numbers):
    answer = set()
    n = len(numbers)
    
    for i in range(n):
        for j in range(i+1, n):
            answer.add(numbers[i]+numbers[j])
    
    answer = list(answer)
    answer.sort()
    
    return answer