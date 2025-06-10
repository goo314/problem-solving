import sys
input = sys.stdin.readline

def chooseFlask(requirements, flaskTypes, markings):
    requirements = sorted(requirements)
    numRequire = len(requirements)

    # initialize
    flaskMarks = [[] for _ in range(flaskTypes)]
    for num, mark in markings:
        flaskMarks[num].append(mark)
    
    ret = 0
    minWaste = 10**9
    for idx in range(flaskTypes):
        # marks = sorted(flaskMarks[idx])
        marks = flaskMarks[idx]
        waste = 0
        i = 0 # index of mark
        j = 0 # index of requirements
        while i < len(marks) and j < numRequire:
            # no need to compute waste
            if minWaste < waste:
                break
            mark = marks[i]
            require = requirements[j]

            if mark < require:
                i += 1
            else:
                waste += mark - require
                j += 1
        
        # can not be used
        if j < numRequire:
            continue

        if waste < minWaste:
            ret = idx
            minWaste = waste
    
    if minWaste == 10**9:
        ret = -1
    
    return ret

n = int(input())
requirements = [int(input()) for _ in range(n)]
flaskTypes = int(input())
totalMarks = int(input())
columns = int(input()) # always 2
markings = [list(map(int, input().split())) for _ in range(totalMarks)]

print(chooseFlask(requirements, flaskTypes, markings))