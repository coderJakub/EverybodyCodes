with open('input.txt') as f:
    content = f.read()
    
grid = content.split('\n\n')[0].split('\n')
tokens = content.split('\n\n')[1].split('\n')

R, C = len(grid), len(grid[0])

def getSlotNumber(col: int) -> int:
    return col // 2 + 1

total = 0

for token in tokens:
    bestWin = 0
    insert = 0
    output = 0
    for i in range(0, C, 2):
        row = -1
        col = i
        instr = token
        
        while row < R-1:
            row += 1
            if grid[row][col] != '*':
                continue
            
            nextMove = instr[0]
            instr = instr[1:]
            col += 1 if col == 0 or (col!=C-1 and nextMove=='R') else -1
        
        if (getSlotNumber(col)*2) - getSlotNumber(i) > bestWin:
            insert = i
            output = col
        bestWin = max((getSlotNumber(col)*2) - getSlotNumber(i), bestWin)
    
    print(f'Best: inSlot->{getSlotNumber(insert)} ({insert}), outSlot->{getSlotNumber(output)} ({output}), {bestWin}')
    total += bestWin
    
print(f'Part 2: {total}') 