def solution(array, commands):
    answer = []
    
    for cmd in commands:
        i, j, k = cmd
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    
    return answer