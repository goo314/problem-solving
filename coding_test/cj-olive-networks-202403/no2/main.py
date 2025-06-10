"""
Description:
    주어진 수열의 연속된 부분 구간 중 가장 긴 등차수열의 길이를 구하여라.
Status:
    주어진 테스트케이스는 다 맞음
My Solution:
    수열 탐색 하면서 
        diff가 같으면 tmp += 1
        다르면 등차수열이 끝났다는 의미이므로 등차수열 최대길이 업데이트 및 tmp 업데이트
"""

def solution(arr):
    answer = 2

    n = len(arr)
    if n == 2:
        return answer
    
    temp = 2
    for i in range(2, n):
        if arr[i-1]-arr[i-2] == arr[i]-arr[i-1]:
            temp += 1
        else:
            answer = max(answer, temp)
            temp = 2

    return answer