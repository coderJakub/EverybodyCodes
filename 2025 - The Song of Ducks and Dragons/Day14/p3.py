import sys
from copy import deepcopy

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read().splitlines()

RC = len(content)
CC = len(content[0])
R = 34
C = 34

startR = (R-RC)//2
startC = (C-CC)//2

def matches(active):
    return all(
        (i,j) in active if x == '#' else (i,j) not in active
        for i, line in enumerate(content, start=startR)
        for j, x in enumerate(line, start=startC)
    )

def round(active: set):
    newActive = set()
    for i in range(R):
        for j in range(C):
            activeN = len([(i+xx, j+yy) for (xx,yy) in [(1,1), (-1,-1), (-1,1), (1,-1), (0,0)] if (i+xx, j+yy) in active])
            if activeN%2==0: newActive.add((i,j))
    return newActive

res = 0
active = set()
seen = []
rounds = 1000000000
for _ in range(rounds):
    active = round(active)
    if active in seen:
        break
    seen.append(active)

idx = seen.index(active)
# full cycles:
res = sum(len(grid) for grid in seen[idx:] if matches(grid))
res *= rounds // (len(seen)-idx)

# before cycle:
res += sum(len(grid) for grid in seen[:idx] if matches(grid))

# last cycle:
res += sum(len(grid) for grid in seen[idx:rounds % (len(seen)-idx)] if matches(grid))

print(res)               