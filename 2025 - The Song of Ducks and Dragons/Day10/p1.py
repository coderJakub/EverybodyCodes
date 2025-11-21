import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read().splitlines()

grid = [[x for x in line] for line in content]
R = len(grid)
L = len(grid[0])

res = 0
queue = [((R-1)//2, (L-1)//2)]
for _ in range(5):
    newQueue = set()
    for (x,y) in queue:
        if grid[x][y] == 'S':
            res += 1
            grid[x][y] = '.'
        for xx, yy in [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]:
            nx, ny = x+xx, y+yy
            if 0 <= nx < R and 0 <= ny < L:
                newQueue.add((nx,ny))
    queue = list(newQueue)
print(res)