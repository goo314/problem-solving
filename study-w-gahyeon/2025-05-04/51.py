def solution(jobs):
    ans = 0
    
    n = len(jobs)
    jobs = [(jobs[i][1], jobs[i][0]) for i in range(n)]
    jobs.sort(key= lambda x: x[0])
    jobs.sort(key= lambda x: x[1])
    
    import heapq
    pq = []
    
    idx = 0
    clock = 0
    while True:
        while idx < n and jobs[idx][1] <= clock:
            heapq.heappush(pq, jobs[idx])
            idx += 1
        
        if not pq:
            clock = jobs[idx][1]
            continue
        
        b, a = heapq.heappop(pq)
        clock += b
        ans += clock - a
        
        if idx >= n and not pq:
            break
    
    return ans // n
