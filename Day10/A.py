with open('in.txt') as f:
    content = f.read().splitlines()

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

print(string)