with open('in.txt') as f:
    lines = f.read().splitlines()
    
dict = {}


targets = []
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if c=='T':
            targets.append([i,j])
        if c=='H':
            targets.append([i,j])
            targets.append([i,j])
        if c=='A':
            dict[(i,j)] = 1
        if c=='B':
            dict[(i,j)] = 2
        if c=='C':
            dict[(i,j)] = 3

max_x = max([x for y,x in targets])

sum = 0
for target in targets:
    found = False
    for key in dict.keys():
        for i in range(1,max_x):
            fall_from = key[0]-i, key[1]+i*2
            for j in range(len(lines)-fall_from[0]):
                x,y = fall_from[0]+j, fall_from[1]+j
                if [x,y] == target:
                    ranking_value = dict[key] * i
                    found = True
                    break
            if found:
                break
        if found:
            break
    sum += ranking_value
print(sum)