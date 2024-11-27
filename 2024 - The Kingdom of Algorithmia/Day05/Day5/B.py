with open('in.txt') as f:
    lines = f.read().splitlines()
    
content = [[] for _ in lines[0].split(' ')]
num = ""
for j,line in enumerate(lines):
    for i,c in enumerate(line.split(' ')):
        if j==0:
            num += c
        content[i].append(int(c))
  
r = 0
rounds = {}
while True:
    r+=1
    row = (r-1)%4
    if len(content[row]) == 0:
        continue
    clapper = content[row].pop(0)
    num = num[:row*2] + str(content[row][0]) + num[(row+1)*2:]
    row = (row+1)%4
    
    cycles = clapper%(len(content[row])*2+1) if clapper//(len(content[row])*2+1)>0 else clapper-1
    column = len(content[row]) - abs(cycles-len(content[row]))
    content[row].insert(column, clapper)
    num = num[:row*2] + str(content[row][0]) + num[(row+1)*2:]
    if num in rounds:
        rounds[num] += 1
    else:
        rounds[num] = 1
    if rounds[num] == 2024:
        break

for k,v in rounds.keys():
    if v == 2024:
        print(int(k)*r)
        break