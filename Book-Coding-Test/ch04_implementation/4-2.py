n = int(input())

# 00:00:00 ~ nn:59:59
# if not including 3 , number of possibilities is 5*9*5*9 = 2025 in one hour
# so , number of possibilities including 3 at least one time is 3600-2025 = 1575
# special cases : when hour is 3, 13, 23

result = 0
if n >= 23:
    result = 1575*(n-2)+3600*3
elif n >= 13:
    result = 1575*(n-1)+3600*2
elif n >= 3:
    result = 1575*n+3600
else:
    result = 1575*(n+1)

print(result)
