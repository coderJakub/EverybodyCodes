import sys
from copy import deepcopy
from functools import cache
fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read().splitlines()

RC = len(content)
CC = len(content[0])
R = 35
C = 35

startR = int(R/2-RC/2)
startC = int(C/2-CC/2)

def matches(active):
    for i, line in enumerate(content, start=startR):
        for j, x in enumerate(line, start=startC):
            if x=='#' and (i,j) not in active or x=='.' and(i,j) in active:
                break
        else:
            break
    else:
        return False
    return True

@cache
def round(active: set):
    newActive = set()
    for i in range(RC):
        for j in range(CC):
            activeN = 0
            for (xx,yy) in [(1,1), (-1,-1), (-1,1), (1,-1)]:
                nx, ny = i+xx, j+yy
                if (nx,ny) in active: activeN += 1
            if (i,j) in active and activeN%2==1:
                newActive.add((i,j))
            elif (i,j) not in active and activeN%2==0:
                newActive.add((i,j))
    return newActive, len(newActive)

res = 0
active = set()
for i,line in enumerate(content):
    for j, x in enumerate(line):
        if x=='#':active.add((i,j))
seen = set()
for _ in range(2025):
    if frozenset(active) in seen:
        break
    seen.add(frozenset(active))
    active, r = round(frozenset(active))
    res += r
print(res)               