with open('in.txt') as f:
    lines = f.read().splitlines()

ins = []
m = []
for line in lines:
    insL = []
    mL = []
    for i in line.split(','):
        insL.append(i[0])
        mL.append(int(i[1:]))
    ins.append(insL)
    m.append(mL)

pos = set()
for j,insL in enumerate(ins):
    start = [0,0,0]
    for i,inst in enumerate(insL):
        match inst:
            case 'U':
                direction = [0,1,0]
            case 'D':
                direction = [0,-1,0]
            case 'L':
                direction = [-1,0,0]
            case 'R':
                direction = [1,0,0]
            case 'F':
                direction = [0,0,1]
            case 'B':
                direction = [0,0,-1]
        for _ in range(m[j][i]):
            start = [start[0]+direction[0],start[1]+direction[1],start[2]+direction[2]]
            pos.add(tuple(start))
print(len(pos))