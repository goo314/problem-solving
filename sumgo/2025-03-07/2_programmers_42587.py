def solution(priorities, location):
    
    from collections import deque
    q = deque()
    n = len(priorities)
    for i in range(n):
        q.append((i, priorities[i]))
    
    ans = 1
    while q:
        cur, p = q.popleft()
        if not q:
            return ans
        if p >= max([p for i, p in q]):
            if cur == location:
                return ans
            ans += 1
        else:
            q.append((cur, p))
    return ans