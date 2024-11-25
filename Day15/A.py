with open('in.txt') as f:
    lines = f.read().splitlines()
    
def bfs(start,grid):
    queue = [(start, 0)]
    visited = set()
    
    while queue:
        print(queue)
        node, dist = queue.pop(0)
        
        if grid[node[0]][node[1]] == 'H':
            return dist*2
        
        visited.add(node)
        
        for dir in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_node = (node[0]+dir[0], node[1]+dir[1])
            if new_node not in visited and grid[new_node[0]][new_node[1]] != '#':
                queue.append((new_node, dist+1))
                
grid = [[c for c in line] for line in lines]

start = [0, lines[0].find('.')]
print(bfs(tuple(start),grid))