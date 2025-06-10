def solution(info, query):
    answer = []
    
    cnt = dict()
    
    for i in info:
        lang, role, level, food, score = i.split(' ')
        
        import itertools
        for i in range(5):
            cases = list(itertools.combinations([0, 1, 2, 3], i))
            for case in cases:
                key = [lang, role, level, food]
                for i in case:
                    key[i] = '-'
                key = ''.join(key)
                if key in cnt:
                    cnt[key].append(int(score))
                else:
                    cnt[key] = [int(score)]
    
    for value in cnt.values():
        value.sort()
    
    for q in query:
        lang, role, level, tmp = q.split(' and ')
        food, score = tmp.split(' ')
        
        key = lang + role + level + food
        if key not in cnt:
            answer.append(0)
            continue
            
        candidate = cnt[key]
        
        l, r = 0, len(candidate)-1
        ans = len(candidate)
        while l <= r:
            mid = (l+r)//2
            if candidate[mid] >= int(score):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        answer.append(len(candidate)-ans)
    
    return answer