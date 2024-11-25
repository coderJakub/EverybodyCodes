with open('in.txt') as f:
    lines = f.read().splitlines()
    
def bfs(start,grid,c):
    queue = [(start, 0, c)]
    
    while queue:
        sorted(queue, key=lambda x: len(x[2]))
        node, dist, found = queue.pop(0)
        
        if found and grid[node[0]][node[1]] in c:
            found.remove(grid[node[0]][node[1]])
        if not found and node[0] == start[0] and node[1] == start[1]:
            return dist   
        
        for dir in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_node = (node[0]+dir[0], node[1]+dir[1])
            if grid[new_node[0]][new_node[1]] != '#' and grid[new_node[0]][new_node[1]] != '~':
                queue.append((new_node, dist+1, found))
                
grid = [[c for c in line] for line in lines]

to_find = set()
for line in grid:
    for c in line:
        if c!='#' and c!='.' and c!='~':
            to_find.add(c)
            
start = [0, lines[0].find('.')]
startS = [0, lines[0].find('.')]
c = ()
sum = 0
print(bfs(tuple(start),grid,to_find))