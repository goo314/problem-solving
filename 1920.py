n = int(input())
arrA = set(map(int, input().split()))

m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num in arrA:
        print(1)
    else:
        print(0)
