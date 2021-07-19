N = int(input())

A = list(map(int, input().split()))

i = 1
while i<N:
    # when nonincreasing
    if A[i-1] >= A[i]:
        break
    i += 1

j = i
while j<N:
    # when nondecreasing
    if A[j-1] <= A[j]:
        break
    j += 1


if j!=N:
    print("NO")
else:
    print("YES")
