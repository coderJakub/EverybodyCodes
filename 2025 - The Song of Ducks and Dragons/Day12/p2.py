import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = [[int(x) for x in line] for line in f.read().splitlines()]

R = len(content)
C = len(content[0])

queue = [(0,0), (R-1, C-1)]
destroyed = set(queue)
while queue:
    x,y = queue.pop(0)
    for xx,yy in [(0,1), (1,0), (-1,0), (0,-1)]:
        nx,ny = x+xx, y+yy
        if 0<=nx<R and 0<=ny<C and content[x][y] >= content[nx][ny] and (nx,ny) not in destroyed:
            destroyed.add((nx,ny))
            queue.append((nx,ny))
            
print(len(destroyed))