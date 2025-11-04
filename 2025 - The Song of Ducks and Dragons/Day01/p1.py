import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read()
    
names = content.split('\n\n')[0].split(',')
instr = content.split('\n\n')[1].split(',')

pos = 0
for el in instr:
    d, n = el[0], int(el[1:])
    pos += n if d=='R' else -n
    pos = min(max(0, pos), len(names)-1)

print(names[pos])