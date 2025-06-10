n, m, k = map(int, input().split())
array = list(map(int, input().split()))

ret = 0
# if number of maximum is bigger than and equal to 2
if array.count(max(array)) >= 2:
    # just the answer is max * m
    ret += max(array) * m
else:
    temp = m//(k+1)
    # I had wrong answer , it should be (k*temp + m%(k+1)) not just (k*temp)
    ret += max(array)*k*temp
    # to find second maximum
    array.remove(max(array))
    ret += max(array)*temp

print(ret)
