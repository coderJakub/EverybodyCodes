import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = [x.split(':')[1] for x in f.read().splitlines()]

res = 0
for i, p1 in enumerate(content):
    for p2 in content[i:]:
        for ch in content:
            if ch == p1 or ch == p2: continue
            if all(c in [a,b] for a,b,c in zip(p1,p2,ch)):
                sim1 = sum(x == y for x,y in zip(p1, ch))                
                sim2 = sum(x == y for x,y in zip(p2, ch))                
                res += sim1*sim2
print(res)