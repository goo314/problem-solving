n, k = map(int, input().split())

nums = [i for i in range(2, n+1)]
while k>0:
    p = min(nums)
    for mp in range(p, n+1, p):
        if mp in nums:
            nums.remove(mp)
            k -= 1
            if k == 0:
                print(mp)
                break
            
