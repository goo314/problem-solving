#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTheGroups' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY queryType
#  3. INTEGER_ARRAY students1
#  4. INTEGER_ARRAY students2
#

def getGroupSize(x, n, edges):
    ret = 0
    visited = [False] * n
    q = []
    q.append(x)
    visited[x] = True
    
    while len(q) > 0:
        x = q.pop(0)
        ret += 1
        
        for y in edges[x]:
            if not visited[y]:
                q.append(y)
                visited[y] = True

    return ret

def getTheGroups(n, queryType, students1, students2):
    # Write your code here
    edges = [[] for _ in range(n)] # edges[v1] = v2
    
    ret = []
    m = len(queryType)
    for i in range(m):
        v1, v2 = students1[i]-1, students2[i]-1
        if queryType[i] == 'Friend':
            edges[v1].append(v2)
            edges[v2].append(v1)
        else: # Total
            g1 = getGroupSize(v1, n, edges)
            g2 = getGroupSize(v2, n, edges)
            ret.append(g1+g2)
    
    return ret

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('myoutput.txt', 'w')

    n = int(input().strip())

    queryType_count = int(input().strip())

    queryType = []

    for _ in range(queryType_count):
        queryType_item = input()
        queryType.append(queryType_item)

    students1_count = int(input().strip())

    students1 = []

    for _ in range(students1_count):
        students1_item = int(input().strip())
        students1.append(students1_item)

    students2_count = int(input().strip())

    students2 = []

    for _ in range(students2_count):
        students2_item = int(input().strip())
        students2.append(students2_item)

    result = getTheGroups(n, queryType, students1, students2)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
