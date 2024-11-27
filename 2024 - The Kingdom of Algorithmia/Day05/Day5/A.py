with open('in.txt') as f:
    lines = f.read().splitlines()
    
content = [[] for _ in lines]
for line in lines:
    for i,c in enumerate(line.split(' ')):
        content[i].append(int(c))
        
def printC():
    for c in content:
        print(c)
    exit()
  
roundsToDo = 10  
rounds = [0 for _ in range(roundsToDo)]
for i in range(len(rounds)):
    row = i%4
    clapper = content[row].pop(0)
    row = (row+1)%4
    column = 0
    for _ in range(clapper-1):
        if column >= len(content[row]):
            row = (row+1)%4
            column = 0
        column += 1
    content[row].insert(column, clapper)
    num =""
    for row in content:
        if len(row) > 0:
            num += str(row[0]) 
    rounds[i] = int(num)
print(rounds[roundsToDo-1])