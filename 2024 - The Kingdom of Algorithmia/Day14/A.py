with open('in.txt') as f:
    lines = f.read()

ins = [inst[0] for inst in lines.split(',')]
m = []
for i in lines.split(','):
    m.append(int(i[1:]))


maxH = 0
curr = 0
for i,inst in enumerate(ins):
    match inst:
        case 'U':
            curr += m[i]
        case 'D':
            curr -= m[i]
    maxH = max(curr,maxH)
    
print(maxH)