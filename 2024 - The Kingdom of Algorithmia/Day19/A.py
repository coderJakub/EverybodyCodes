with open('in.txt') as f:
    contentF = f.read()
    
key = contentF.splitlines()[0]
grid = [list(line) for line in contentF.splitlines()[2:]]

def calc(key,grid):
    index = 0
    while True:
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                rotationPoint = (i,j)
                print(rotationPoint, key[index])
                #rotate all 8 neighbors of rotationPoint clockwise (R) (0,1 gets 0,2, ...) or counterclockwise (L)
                match key[index]:
                    case 'R':
                        neighbors_l = [[i+x,j+y] for x,y in [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]]
                        buf = grid[neighbors_l[7][0]][neighbors_l[7][1]]
                        for k in range(7,0,-1):
                            grid[neighbors_l[k][0]][neighbors_l[k][1]] = grid[neighbors_l[k-1][0]][neighbors_l[k-1][1]]
                        grid[neighbors_l[0][0]][neighbors_l[0][1]] = buf  
                            
                    case 'L':
                        neighbors_l = [[i+x,j+y] for x,y in [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]]
                        buf = grid[neighbors_l[7][0]][neighbors_l[7][1]]
                        for k in range(7,0,-1):
                            grid[neighbors_l[k][0]][neighbors_l[k][1]] = grid[neighbors_l[k-1][0]][neighbors_l[k-1][1]]
                        grid[neighbors_l[0][0]][neighbors_l[0][1]] = buf                    
                for line in grid:
                    print(line)
                index = (index+1)%len(key)
                for line in grid:
                    if '<' in line and '>' in line:
                        return grid

grid = calc(key,grid)
for i,line in enumerate(grid):
    if '<' in line:
        openT = line.index('>')
        closeT = line.index('<')
        string = ''.join(line[openT+1:closeT])
        print(string)
        break