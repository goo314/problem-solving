def solution(n, times):
    answer = 0
    
    l, r = 1, n*min(times)
    while l <= r:
        mid = (l+r)//2
        tmp = 0
        for t in times:
            tmp += mid//t
        if tmp >= n:
            answer = mid
            r = mid-1
        else:
            l = mid+1
        
    return answer