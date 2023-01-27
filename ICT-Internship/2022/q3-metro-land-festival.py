import sys
input = sys.stdin.readline

def minimizeCost(numPeople, x, y):
    n = len(x)
    size = max(max(x), max(y))
    city = [0]*(size*size)
    
    for a in range(1, size+1):
        for b in range(1, size+1):
            dist = 0            
            for i in range(n):
                xi = x[i]
                yi = y[i]
                dist += (abs(xi-a) + abs(yi-b)) * numPeople[i]
            city[(a-1)*size + (b-1)] = dist
    
    ret = min(city)
    return ret

n = int(input())
numPeople = [int(input()) for _ in range(n)]

m = int(input())
x = [int(input()) for _ in range(m)]

m = int(input())
y = [int(input()) for _ in range(m)]

print(minimizeCost(numPeople, x, y))