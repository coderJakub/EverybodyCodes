import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read().splitlines()

def checkTurn(grid: list, queue: list) -> int:
    res = 0
    for (x,y) in queue: 
        if grid[x][y] == 'S' and (x,y) not in hides:
            res += 1
            grid[x][y] = '.'
    return res

grid = [[x if x!='#' else '.' for x in line] for line in content]
hides = []
for i, line in enumerate(content):
    for j, x in enumerate(line):
        if x=='#': hides.append((i,j))
R = len(content)
L = len(content[0])

res = 0
queue = [((R-1)//2, (L-1)//2)]
for k in range(20):
    newQueue = set()
    for (x,y) in queue:
        for xx, yy in [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]:
            nx, ny = x+xx, y+yy
            if 0 <= nx < R and 0 <= ny < L:
                newQueue.add((nx,ny))

    queue = list(newQueue)
    res += checkTurn(grid, queue)
    grid.insert(0, ['.' for x in range(L)])
    grid.pop()
    res += checkTurn(grid, queue)

print(res)