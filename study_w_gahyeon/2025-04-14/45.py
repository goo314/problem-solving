def solution(progresses, speeds):
    ans = []
    
    n = len(progresses)
    periods = []
    for i in range(n):
        p, s = progresses[i], speeds[i]
        d = (100-p)//s
        if (100-p)%s > 0:
            d += 1
        periods.append(d)
    
    m, cnt = periods[0], 1
    for i in range(1, n):
        if m < periods[i]:
            ans.append(cnt)
            m, cnt = periods[i], 1
        else:
            cnt += 1
    ans.append(cnt)
    
    return ans
