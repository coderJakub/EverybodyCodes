with open('in.txt') as f:
    contentF = f.read().splitlines()

colL = len(contentF)
lineL = len(contentF[0])

grid = {(i, j): contentF[i][j] for i in range(colL) for j in range(lineL)}

def bfs(start):
    queue = [(start, 0, 1000)]
    
    while queue:
        (i, j), dist, fuel = max(queue, key=lambda x: x[2] if x[1] > 20 else x[1])
        queue.remove(((i, j), dist, fuel))
        
        if dist == 100:
            return fuel, i, j
        
        for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]: 
            if 0 <= x < colL and 0 <= y < lineL and fuel > 0 and grid[(x, y)] not in ['S','#']:
                if grid[(x, y)] == '.':
                    queue.append(((x, y), dist+1, fuel-1))
                elif grid[(x, y)] == '-':
                    queue.append(((x, y), dist+1, fuel-2))
                elif grid[(x, y)] == '+':
                    queue.append(((x, y), dist+1, fuel+1))

for gridK in grid.keys():
    if grid[gridK] == 'S':
        start = gridK
        break
print(bfs(start))
        