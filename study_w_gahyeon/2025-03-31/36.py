def solution(numbers):
    answer = -1
    under10 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    tmp = under10 - set(numbers)
    answer = sum(list(tmp))
    return answer
