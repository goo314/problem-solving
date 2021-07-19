N = input()
count = [0 for _ in range(10)]

for i in range(len(N)):
    dgt = int(N[i])
    count[dgt] += 1

avg = (count[6]+count[9])//2
if (count[6]+count[9])%2 == 1:
    avg += 1

count[6], count[9] = avg, avg

print(max(count))
