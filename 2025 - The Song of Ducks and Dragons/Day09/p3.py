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
found = []    
for i, fam1 in enumerate(families):
    if i in found: continue
    newFam = set(fam1)
    found.append(i)
    changes = True
    while changes:
        changes = False
        for j, fam2 in enumerate(families[i:], start=i):
            if j in found: continue
            if any(x in newFam for x in fam2):
                changes = True
                for x in fam2: newFam.add(x)
                found.append(j)
    fams.append(newFam)

res = sum(list(max(fams)))
print(res)