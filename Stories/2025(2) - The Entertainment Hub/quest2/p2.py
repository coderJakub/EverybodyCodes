with open('in.txt') as f:
    content = f.read()

content *=100000
col = 0
total = 0
while len(content)>0:
    first = content[0]
    content = content[1:]
    
    if ((col == 0 and first=='R') or (col == 1 and first=='G') or (col == 2 and first=='B')) and len(content)%2==1:
        content = content[:(len(content)//2)] + content[(len(content)//2)+1:]
    col += 1
    col = col%3
    total += 1
    print(len(content))
    
print(total)
        
        