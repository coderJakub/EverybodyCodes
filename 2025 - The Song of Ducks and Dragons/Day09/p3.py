import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = [x.split(':')[1] for x in f.read().splitlines()]

res = 0
families = []
for i, p1 in enumerate(content):
    for j, p2 in enumerate(content[i:], start=i):
        for k, ch in enumerate(content):
            if ch == p1 or ch == p2: continue
            for a,b,c in zip(p1,p2,ch):
                if c not in [a, b]:
                    break
            else:
                families.append((i+1, j+1, k+1))

fams = []        
for p1, p2, ch in families:
    for fam in fams:
        if p1 in fam or p2 in fam or ch in fam:
            fam.add(p1)
            fam.add(p2)
            fam.add(ch)
    else:
        fams.append(set([p1,p2,ch]))
                
                    
biggestFam = max(fams)
res = sum(list(biggestFam))
print(res)