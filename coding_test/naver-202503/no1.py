"""
Description:
    총: cylinder = [1: 총알있음 or 0: 총알없음]
    현재 몇번쨰 총알인지 모르지만 총알이 없다는 것을 확인했을 때, 다음 a번을 발사할 때 모두 총알이 발사되지 않을 확률을 기약분수로 나타내라.
    다음 총알은 현재 인덱스+1 이고 인덱스가 cylinder 크기(n)보다 크면 1번째로 돌아간다.
Status:
    주어진 테스트케이스는 다 맞음
My Solution:
    cylinder을 돌면서
        q: 현재 총알이 없는 경우를 모두 더하고
        p: (i, i+a+1) 다음 총알에 대해 총알이 없는 경우(=set 연산 길이가 1이고 0이 들어 있는 경우)를 구하고
    유클리드 호제법으로 p와 q의 최대 공약수를 구한 후 p/q를 리턴
"""

def solution(cylinder, a):
    n = len(cylinder)
    p, q = 0, 0
    for i in range(n):
        if cylinder[i] == 0:
            q += 1
            if i+a < n:
                tmp = set(cylinder[i:i+a+1])
            else:
                tmp = set(cylinder[i:n]+cylinder[:(i+a+1)%n])
            if len(tmp) == 1 and 0 in tmp:
                p += 1
    
    a, b = p, q
    while b != 0:
        a, b = b, a%b
        a, b = max(a, b), min(a, b)
    
    ans = [p//a, q//a]
    return ans

# 테스트케이스
cylinder = [1, 0, 0, 0, 0, 1]
a = 2
print([1, 2] == solution(cylinder, a))