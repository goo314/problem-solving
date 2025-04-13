def solution(bridge_length, weight, truck_weights):
    ans = 0
    
    from collections import deque
    q = deque()
    
    cnt, bridge_w, truck_i = 0, 0, 0
    n = len(truck_weights)
    for i in range(bridge_length*(n+1)):
        if cnt == n:
            ans = i
            break
        if len(q) > 0 and q[0][1] == i-bridge_length:
            w, t = q.popleft()
            cnt += 1
            bridge_w -= w
        if truck_i < n and bridge_w + truck_weights[truck_i] <= weight:
            q.append((truck_weights[truck_i], i))
            bridge_w += truck_weights[truck_i]
            truck_i += 1
    
    return ans
