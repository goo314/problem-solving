def solution(input_string):
    ans = []
    
    n = len(input_string)
    cnt = [0] * 26
    cnt[ord(input_string[0]) - ord('a')] += 1
    for i in range(1, n):
        j = ord(input_string[i]) - ord('a')
        if cnt[j] > 0 and input_string[i] != input_string[i-1]:
            ans.append(input_string[i])
        cnt[j] += 1
    ans = list(set(ans))
    ans.sort()
    if len(ans) == 0:
        ans = 'N'
    else:
        ans = ''.join(ans)
    
    return ans