def solution(gems):
    n = len(gems)
    m = len(set(gems))
    
    ans = [1, n]
    from collections import defaultdict
    d = defaultdict(int)
    
    l = 0
    for r in range(n):
        d[gems[r]] += 1
        
        while len(d) == m:
            if r-l < ans[1]-ans[0]:
                ans = [l+1, r+1]
            
            d[gems[l]] -= 1
            if d[gems[l]] == 0:
                del d[gems[l]]
            l += 1
    
    return ans
