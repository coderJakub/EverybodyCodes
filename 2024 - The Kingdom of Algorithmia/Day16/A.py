with open('in.txt') as f:
    lines = f.read().splitlines()
    
leverAdj = [int(lever) for lever in lines[0].split(',')]
lines.pop(0)
lines.pop(0)

spinners = [[] for _ in range(len(lines[0].split(' ')))]
for line in lines:
    j=0
    for i in range(len(spinners)):
        if not ' ' in list(line[j:j+3]) and not '' == line[j:j+3]:
            spinners[i].append(line[j:j+3])
        j+=4

for i in range(100):
    for j, lever in enumerate(leverAdj):
        print(spinners)
        for k in range(lever):
            spinners[j] = [spinners[j][1]] + spinners[j][2:] + [spinners[j][0]]
            print(spinners)
        print()

for i in spinners:
    print(i[0], end=' ')