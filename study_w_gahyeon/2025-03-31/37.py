def solution(participant, completion):
    
    d = dict()
    for p in participant:
        if p in d:
            d[p] += 1
        else:
            d[p] = 1
    
    for c in completion:
        d[c] -= 1
    
    for k in d:
        if d[k] != 0:
            return k
    return
