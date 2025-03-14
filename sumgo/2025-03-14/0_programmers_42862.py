def solution(n, lost, reserve):
    nl, nr = len(lost), len(reserve)
    
    lost.sort()
    reserve.sort()
    i, j = 0, 0
    
    ans = n - nl
    
    tmp = list(set(lost).intersection(set(reserve)))
    ans += len(tmp)
    
    while i < nl and j < nr:
        if lost[i] in tmp:
            i += 1
            continue
        if reserve[j] in tmp:
            j += 1
            continue
        if abs(lost[i]-reserve[j]) == 1:
            i += 1
            j += 1
            ans += 1
        elif lost[i] < reserve[j]:
            i += 1
        else:
            j += 1
    return ans