def solution(orders, course):
    answer = []
    
    dp = dict()
    dp_cnt = dict()
    import itertools
    for order in orders:
        for c in course:
            for case in list(itertools.combinations(list(order), c)):
                case = ''.join(sorted(list(case)))
                if case in dp:
                    dp[case] += 1
                else:
                    dp[case] = 1
                
                if len(case) in dp_cnt:
                    dp_cnt[len(case)] = max(dp_cnt[len(case)], dp[case])
                else:
                    dp_cnt[len(case)] = dp[case]
                
    dp = list(dp.items())
    
    for menu, cnt in dp:
        if cnt >= 2 and cnt == dp_cnt[len(menu)]:
            answer.append(''.join(menu))
            
    answer.sort()

    return answer