with open('in.txt') as f:
    lines = f.read().splitlines()
    
content = [list(line) for line in lines]

def dijkstra(grid, start, end):
    def getNeighbors(node):
        neighbors = []
        for k in [-1, 0], [1, 0], [0, -1], [0, 1]:
            i, j = k
            if 0 <= node[0]+i < len(grid) and 0 <= node[1]+j < len(grid[0]) and grid[node[0]+i][node[1]+j] != '#':
                neighbors.append((node[0]+i, node[1]+j))
        return neighbors
    def getDistance(node):
        return abs(node[0]-start[0]) + abs(node[1]-start[1])
    def getCost(node, current, grid):
        cv = int(grid[current[0]][current[1]])
        nv = int(grid[node[0]][node[1]])
        for i in range(8):
            if (cv+i)%10 == nv or (cv-i)%10 == nv:
                return i+1
    def reconstructPath(cameFrom, current):
        totalPath = [current]
        while current in cameFrom:
            current = cameFrom[current]
            totalPath.append(current)
        for node in totalPath:
            print(node, gScore[node], int(grid[node[0]][node[1]]))
        return totalPath
    openSet = {start}
    closedSet = set()
    cameFrom = {}
    gScore = {start: 0}
    #fScore = {start: getDistance(start)}
    while openSet:
        current = min(openSet, key=lambda x: gScore[x])
        
        if current == end:
            reconstructPath(cameFrom, current)
            return gScore[current]
        
        openSet.remove(current)
        
        closedSet.add(current)
        
        for neighbor in getNeighbors(current):
            if neighbor in closedSet:
                continue
            
            tentativeGScore = gScore[current] + getCost(neighbor,current,grid)
            
            if neighbor not in openSet:
                openSet.add(neighbor)
                
            elif tentativeGScore >= gScore[neighbor]:
                continue
            
            cameFrom[neighbor] = current
            gScore[neighbor] = tentativeGScore
            #fScore[neighbor] = gScore[neighbor] + getDistance(neighbor)
    return None

for i,line in enumerate(content):
    for j, c in enumerate(line):
        if c == 'S':
            start = (i, j)
            content[i][j] = '0'
        elif c == 'E':
            end = (i, j)
            content[i][j] = '0'
print(dijkstra(content, start, end))