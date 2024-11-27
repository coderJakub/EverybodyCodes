with open('in.txt') as f:
    contentF = f.read()

def getRunicPower(string):
    power = 0
    for i,c in enumerate(string):
        power += (ord(c)-ord('A')+1)*(i+1)
    return power

contents = []
for sampleRow in contentF.split('\n\n'):
    for i in range(15):
        content = []
        for row in sampleRow.splitlines():
            content.append(row[i*8+i:(i+1)*8+i])
        contents.append(content)     

count = 0
for content in contents:
    grid = [[c for c in line] for line in content]
    string = ''
    recoverPoint = [1,1]
    for i in range(4):
        recoverPoint = [recoverPoint[0] + 1, 1]
        rowChar = set()
        for c in grid[recoverPoint[0]]:
            rowChar.add(c)
        for j in range(4):
            recoverPoint = [recoverPoint[0], recoverPoint[1] + 1]
            columnChar = set()
            for row in grid:
                columnChar.add(row[recoverPoint[1]])
            for c in rowChar:
                if c in columnChar and c != '.':
                    string += c
                    break
    count += getRunicPower(string)

print(count)