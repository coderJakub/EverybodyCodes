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
                er = True
                for k in range(-1,2):
                    if i+k<0 or i+k>=len(grid):
                        er = False
                        break
                    for l in range(-1,2):
                        if j+l<0 or j+l>=len(line):
                            er = False
                            break
                        if grid[i+k][j+l]<count:
                            er = False
                grid[i][j] = count+1 if er else count
    if oldGrid == grid:
        break

sum = sum([sum(line) for line in grid])
print(sum)