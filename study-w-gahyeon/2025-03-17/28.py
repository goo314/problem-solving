def solution(numbers):
    answer = ''
    
    numbers = [121, 12]
    numbers = list(map(str, numbers))
    numbers.sort(key= lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    if answer[0] == '0':
        answer = '0'
    
    return answer