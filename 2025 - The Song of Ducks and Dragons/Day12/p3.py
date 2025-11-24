import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = [[int(x) for x in line] for line in f.read().splitlines()]

R = len(content)
C = len(content[0])

def chainReaction(destroyed: set):
    possib = []
    for i in range(R):
        for j in range(C):
            currDestroyed = destroyed.copy()
            queue = [(i,j)]
            currDestroyed.add(queue[0])
            while queue:
                x,y = queue.pop(0)
                for xx,yy in [(0,1), (1,0), (-1,0), (0,-1)]:
                    nx,ny = x+xx, y+yy
                    if 0<=nx<R and 0<=ny<C and content[x][y] >= content[nx][ny] and (nx,ny) not in currDestroyed:
                        currDestroyed.add((nx,ny))
                        queue.append((nx,ny))
            possib.append(currDestroyed)
    return possib
    
destroyed = set()
for i in range(3):
    destroyed = max(chainReaction(destroyed), key=len)
            
print(len(destroyed))