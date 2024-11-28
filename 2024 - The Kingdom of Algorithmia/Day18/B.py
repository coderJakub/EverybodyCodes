with open('in.txt') as f:
    contentF = f.read().splitlines()
    
grid = [[c for c in line] for line in contentF]

starts = [[1,0],[len(grid)-2,len(grid[0])-1]]
p_s = []
for i,row in enumerate(grid):
    for j,c in enumerate(row):
        if c=='P':
            p_s.append([i,j])

def fillWater(grid, starts, p_s):
    queue = [[start,0] for start in starts]
    visited = set()
    while queue:
        [x,y],dist = queue.pop(0)
        visited.add((x,y))
        if [x,y] in p_s:
            p_s.remove([x,y])
        if not p_s:
            return dist
        for i,j in [[1,0],[0,1],[-1,0],[0,-1]]:
            if y+j >= 0 and y+j < len(grid[0]) and (x+i,y+j) not in visited and grid[x+i][y+j] != '#':
                queue.append([[x+i,y+j],dist+1])

print(fillWater(grid, starts, p_s))