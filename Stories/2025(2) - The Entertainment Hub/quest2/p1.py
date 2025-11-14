with open('in.txt') as f:
    content = f.read()

col = 0
total = 0
while len(content)>0:
    while len(content)>0:
        first = content[0]
        content = content[1:]
        
        if (col == 0 and first!='R') or (col == 1 and first!='G') or (col == 2 and first!='B'):
            #print(col)
            #print(first)
            #print()
            break
        #print(col)
    col += 1
    col = col%3
    total += 1
    
print(total)
        
        