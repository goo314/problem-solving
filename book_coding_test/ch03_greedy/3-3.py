n, m = map(int, input().split())
cards = list()
# It is more convenient to calculating while having input
for _ in range(n):
    row = list(map(int, input().split()))
    cards.append(row)

ret = -1
# It expresses easier when using 'for c in cards'
for i in range(n):
    # ret = max(ret, min(cards[i]))
    if min(cards[i]) > ret:
        ret = min(cards[i])

print(ret)

