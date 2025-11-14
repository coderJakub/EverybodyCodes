with open('input.txt') as f:
    content = f.read()
    
grid = content.split('\n\n')[0].split('\n')
tokens = content.split('\n\n')[1].split('\n')

R, C = len(grid), len(grid[0])

def getSlotNumber(col: int) -> int:
    return col // 2 + 1

total = 0
insertCol = 0

for token in tokens:
    row = -1
    col = insertCol
    
    while row < R-1:
        row += 1
        if grid[row][col] != '*':
            continue
        
        nextMove = token[0]
        token = token[1:]
        col += 1 if col == 0 or (col!=C-1 and nextMove=='R') else -1
    
    total += max((getSlotNumber(col)*2) - getSlotNumber(insertCol), 0)
    insertCol += 2
    
print(f'Part 1: {total}') 