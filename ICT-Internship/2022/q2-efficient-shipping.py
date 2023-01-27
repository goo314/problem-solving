import sys
input = sys.stdin.readline

def getMaxUnits(boxes, unitsPerBox, truckSize):
    ret = 0
    size = truckSize
    
    ## greedy
    # while size > 0 and len(boxes) > 0:
    #     unit = max(unitsPerBox)
    #     idx = unitsPerBox.index(unit)
    #     num = boxes[idx]

    #     if size < num:
    #         ret += unit * size
    #         size -= size
    #     else:
    #         ret += unit * num
    #         size -= num
        
    #     del boxes[idx]
    #     del unitsPerBox[idx]

    boxInfo = list(zip(unitsPerBox, boxes))
    boxInfo = sorted(boxInfo, key=lambda x: -x[0])

    pos = 0
    while size > 0 and pos < len(boxInfo):
        unit, num = boxInfo[pos][0], boxInfo[pos][1]
        
        if size < num:
            ret += unit * size
            size -= size
        else:
            ret += unit * num
            size -= num
        
        pos += 1

    return ret

n = int(input())
boxes = [int(input()) for _ in range(n)]
n = int(input())
unitsPerBox = [int(input()) for _ in range(n)]
truckSize = int(input())

print(getMaxUnits(boxes, unitsPerBox, truckSize))