import sys
from copy import deepcopy

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read().splitlines()
    
grid = [[x for x in line] for line in content]
R = len(grid)
C = len(grid[0])

res = 0
for _ in range(10):
    newGrid = deepcopy(grid)
    for i, line in enumerate(grid):
        for j, x in enumerate(line):
            activeN = 0
            for (xx,yy) in [(1,1), (-1,-1), (-1,1), (1,-1)]:
                nx, ny = i+xx, j+yy
                if not 0<= nx < R or not 0<= ny < C:
                    continue
                if grid[nx][ny]=='#': activeN += 1
            if x=='#' and activeN%2==0:
                newGrid[i][j] = '.'
            elif x=='.' and activeN%2==0:
                newGrid[i][j] = '#'
            if newGrid[i][j] == '#': res+=1
    grid = deepcopy(newGrid)
print(res)               