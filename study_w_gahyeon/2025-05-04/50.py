def solution(operations):

    import heapq
    deleted = dict()
    minh, maxh = [], []
    
    id = 0
    for oper in operations:
        op, num = oper[0], int(oper[2:])
        if op == "I":
            heapq.heappush(minh, (num, id))
            heapq.heappush(maxh, (-num, id))
            deleted[id] = False
            id += 1
        elif op == "D" and num == 1:
            while maxh:
                maxid = heapq.heappop(maxh)[1]
                if not deleted[maxid]:
                    deleted[maxid] = True
                    break
        elif op == "D" and num == -1:
            while minh:
                minid = heapq.heappop(minh)[1]
                if not deleted[minid]:
                    deleted[minid] = True
                    break
    
    ans = [0, 0]
    while maxh:
        num, id = heapq.heappop(maxh)
        if not deleted[id]:
            ans[0] = -num
            break
    while minh:
        num, id = heapq.heappop(minh)
        if not deleted[id]:
            ans[1] = num
            break

    return ans
