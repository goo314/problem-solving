'''
우선순위 큐를 이용한다.
(가장 적은 시간)*(남아있는 음식의 개수)를 빼면서 진행한다.
(전체시간)%(남아있는 음식의 개수)를 출력한다.
'''
import sys
import heapq
input = sys.stdin.readline

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) # (time, index)
    
    sum_value = 0 # 먹은 시간
    previous = 0

    length = len(food_times)
    while sum_value + ((q[0][0]-previous)*length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous)*length
        length -= 1
        previous = now
    
    answer = sorted(q, key=lambda x: x[1])
    return answer[(k-sum_value)%length][1]

food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times, k))