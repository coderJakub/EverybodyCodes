with open('in.txt') as f:
    contentF = f.read()
    
key = contentF.splitlines()[0]
grid = [list(line) for line in contentF.splitlines()[2:]]

def calc(key,grid):
    for s in range(100):
        index = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                rotationPoint = (i,j)
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
                index = (index+1)%len(key)                
    return grid

grid = calc(key,grid)
for i,line in enumerate(grid):
    if '<' in line:
        openT = line.index('>')
        closeT = line.index('<')
        string = ''.join(line[openT+1:closeT])
        print(string)
        break