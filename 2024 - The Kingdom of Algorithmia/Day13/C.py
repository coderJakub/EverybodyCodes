with open('in.txt') as f:
    lines = f.read().splitlines()
    
content = [list(line) for line in lines]

def dijkstra(grid, starts, end):
    # Return neighbors of node
    def getNeighbors(node):
        neighbors = []
        for k in [-1, 0], [1, 0], [0, -1], [0, 1]:
            i, j = k
            if 0 <= node[0]+i < len(grid) and 0 <= node[1]+j < len(grid[0]) and grid[node[0]+i][node[1]+j] != '#':
                neighbors.append((node[0]+i, node[1]+j))
        return neighbors
    
    # Return cost of moving from current to node
    def getCost(node, current, grid):
        cv = int(grid[current[0]][current[1]])
        nv = int(grid[node[0]][node[1]])
        for i in range(8):
            if (cv+i)%10 == nv or (cv-i)%10 == nv:
                return i+1
    openSet = set()
    closedSet = set()
    cameFrom = {}
    score = {}
    
    #Add all starting points to the open set finds automatically the one with the lowest score
    for start in starts:
        openSet.add(start)
        score[start] = 0
        
    while openSet:
        #Get the node with the lowest score
        current = min(openSet, key=lambda x: score[x])
        
        if current == end:
            return score[current]
        
        # Remove from the open set and add to the closed set -> closed set includes all nodes that have been visited
        openSet.remove(current)
        closedSet.add(current)
        
        for neighbor in getNeighbors(current):
            if neighbor in closedSet:
                continue
            
            tentativescore = score[current] + getCost(neighbor,current,grid)
            
            if neighbor not in openSet:
                openSet.add(neighbor)
                
            elif tentativescore >= score[neighbor]:
                continue
            
            cameFrom[neighbor] = current
            score[neighbor] = tentativescore

starts = []
for i,line in enumerate(content):
    for j, c in enumerate(line):
        if c == 'S':
            starts.append((i, j))
            content[i][j] = '0'
        elif c == 'E':
            end = (i, j)
            content[i][j] = '0'
            
            
print(dijkstra(content, starts, end))