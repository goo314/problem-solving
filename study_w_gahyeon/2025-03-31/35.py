def solution(before, after):
    cnt = [0]*26
    
    for b in before:
        cnt[ord(b)-ord('a')] += 1
    for a in after:
        cnt[ord(a)-ord('a')] -= 1
        
    for c in cnt:
        if c != 0:
            return 0
    return 1
