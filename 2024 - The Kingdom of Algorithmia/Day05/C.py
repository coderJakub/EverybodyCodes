with open('in.txt') as f:
    lines = f.read().splitlines()
    
content = [[] for _ in lines[0].split(' ')]
for j,line in enumerate(lines):
    for i,c in enumerate(line.split(' ')):
        content[i].append(int(c))
  
r = 0
b = 4
max = 0
while True:
    row = r%4
    r+=1
    if len(content[row]) == 0:
        continue
    clapper = content[row].pop(0)
    row = (row+1)%4
    
    cycles = (clapper-1)%(len(content[row])*2)
    column = len(content[row]) - abs(cycles-len(content[row]))
    content[row].insert(column, clapper)
    num = ""
    for row in content:
        if len(row) > 0:
            num += str(row[0])
    if int(num) > max:
        max = int(num)
        print(max)