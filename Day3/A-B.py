from copy import deepcopy

with open('in.txt') as f:
    lines = f.read().splitlines()

grid = [[int(c)for c in line.replace('#','1').replace('.','0')] for line in lines]

count = 0
while True:
    oldGrid = deepcopy(grid)
    count += 1
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == count:
                if (grid[i][j+1]>=count and
                    grid[i][j-1]>=count and
                    grid[i+1][j]>=count and
                    grid[i-1][j]>=count
                ):
                    grid[i][j] = count+1
    if oldGrid == grid:
        break
    
sum = sum([sum(line) for line in grid])
print(sum)