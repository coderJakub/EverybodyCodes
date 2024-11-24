with open('in.txt') as f:
    lines = f.read().splitlines()

grid = set()
leaves = set()
for line in lines:
    instructions = [i[0] for i in line.split(',')]
    amount = [int(i[1:]) for i in line.split(',')]

    place = [0,-1,0]
    for i,instruction in enumerate(instructions):
        
        match instruction:
            case 'U': direction = [0,1,0]
            case 'D': direction = [0,-1,0]
            case 'L': direction = [-1,0,0]
            case 'R': direction = [1,0,0]
            case 'F': direction = [0,0,1]
            case 'B': direction = [0,0,-1]
        for i in range(amount[i]):
            place = [place[j]+direction[j] for j in range(3)]
            grid.add(tuple(place))
    leaves.add(tuple(place))

def bfs(grid, start, end):
    queue = [(start,0)]
    visited = set()

    while queue:
        node,dist = queue.pop(0)
        if node == end:
            return dist
        if node in visited:
            continue
        visited.add(node)
        
        for dir in [[0,1,0],[0,-1,0],[-1,0,0],[1,0,0],[0,0,1],[0,0,-1]]:
            nextNode = tuple([node[i]+dir[i] for i in range(3)])
            if nextNode in grid:
                queue.append((nextNode,dist+1))
maxH = max([l[1] for l in leaves])
minH = min([l[1] for l in leaves])

maxSt = max([g[1] if g[0]==0 and g[2]==0 else 0 for g in grid])

maxH = min(maxH,maxSt)

minSum=100000
for h in range(minH,100):
    sum = 0
    for l in leaves:
        sum += bfs(grid, (0,h,0), l)
    minSum = min(minSum, sum)
print(minSum)