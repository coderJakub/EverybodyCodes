with open('in.txt') as f:
    lines = f.read().splitlines()
    
content = [list(line) for line in lines]

def bfs(content, start, end):
    queue = [(start, 0, [start])]
    
    while queue:
        (x, y), dist, path = queue.pop(0)
        if dist > 100:
            print('Too long')
        
        if (x, y) == end:
            return dist
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(content) and 0 <= ny < len(content[0]) and not content[nx][ny] in '#' and (nx, ny) not in path:
                i=0
                for i in range(len(queue)):
                    if queue[i][1] >= dist + abs(int(content[x][y])-int(content[nx][ny]))+1:
                        break
                queue.insert(i+1, ((nx, ny), dist + abs(int(content[x][y])-int(content[nx][ny]))+1, path + [(nx, ny)]))
for i,line in enumerate(content):
    for j, c in enumerate(line):
        if c == 'S':
            start = (i, j)
            content[i][j] = '0'
        elif c == 'E':
            end = (i, j)
            content[i][j] = '0'
print(end, start)
print(bfs(content, start, end))