"""택배배달과 수거하기

Algorithm: 
    Greedy
Level :
    Level 2
Status:
    Pass
Tag:
    CJ올리브네트웍스
"""


def solution(cap, n, deliveries, pickups):
    answer = 0
    
    i, j = n-1, n-1
    
    while i>=0 and deliveries[i] == 0:
        i -= 1
    while j>=0 and pickups[j] == 0:
        j -= 1
    answer += (max(i, j)+1)*2
    
    while i>=0 or j>=0:
        deliver, pickup = cap, cap
        while i>=0 and deliver >= 0:
            temp = deliver
            deliver -= deliveries[i]
            deliveries[i] = max(0, deliveries[i]-temp)
            if deliveries[i] == 0:
                i -= 1
        while j>=0 and pickup >= 0:
            temp = pickup
            pickup -= pickups[j]
            pickups[j] = max(0, pickups[j]-temp)
            if pickups[j] == 0:
                j -= 1
        
        answer += (max(i, j)+1) * 2

    return answer