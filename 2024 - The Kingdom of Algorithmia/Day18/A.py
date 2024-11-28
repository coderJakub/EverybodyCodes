with open('in.txt') as f:
    contentF = f.read().splitlines()
    
grid = [[c for c in line] for line in contentF]

start = [1,0]
sum = 0
for row in grid:
    for c in row:
        if c=='P':
            sum += 1

def fillWater(grid, start, num):
    queue = [[start,0]]
    visited = set()
    found = 0
    while queue:
        [x,y],dist = queue.pop(0)
        visited.add((x,y))
        if grid[x][y] == 'P':
            found +=1
            if found == num:
                return dist
        for i,j in [[1,0],[0,1],[-1,0],[0,-1]]:
            if y+j >= 0 and (x+i,y+j) not in visited and grid[x+i][y+j] != '#':
                queue.append([[x+i,y+j],dist+1])

print(fillWater(grid, start, sum))