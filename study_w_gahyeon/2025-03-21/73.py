def solution(ability):
    
    n = len(ability) # students
    m = len(ability[0]) # number of abilities
    
    from itertools import permutations
    cases = list(permutations(range(n)))
    ans = 0
    
    for case in cases:
        tmp = 0
        for i in range(m):
            tmp += ability[case[i]][i]
        ans = max(ans, tmp)
    
    return ans