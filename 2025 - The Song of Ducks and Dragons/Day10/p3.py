import sys
from functools import cache

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read().splitlines()

hides = set()
sheeps = []
dragon = None
for i, line in enumerate(content):
    for j, x in enumerate(line):
        if x=='#': hides.add((i,j))
        if x=='S': sheeps.append((i,j))
        if x=='D': dragon = (i,j)
sheeps = tuple(sheeps)

R = len(content)
L = len(content[0])

def getMovesD(x,y):
    movesD = [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]
    moves = []
    for xx, yy in movesD:
        nx, ny = x+xx,y+yy
        if 0 <= nx < R and 0 <= ny < L:
            moves.append((nx,ny))
    return moves

@cache
def dfs(sheeps: tuple[tuple], dragon: tuple, turn='S'):
    res = 0
    changes = 0
    if turn == 'S':
        if not sheeps: return 1
        for i,(x,y) in enumerate(sheeps):
            nx = x+1
            if nx == R: 
                changes += 1
            elif (nx,y) != dragon or (nx,y) in hides:
                changes += 1
                res += dfs(tuple(sheeps[:i] + ((nx,y),) + sheeps[i+1:]), dragon, 'D')
    if turn == 'D' or changes == 0:
        x,y = dragon
        for nx,ny in getMovesD(x,y):
            res += dfs(tuple(s for s in sheeps if s != (nx,ny) or s in hides), (nx,ny), 'S')
    return res
                            
print(dfs(sheeps, dragon))