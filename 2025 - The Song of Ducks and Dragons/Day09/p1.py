import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = [x[2:] for x in f.read().splitlines()]

res = 0
for child in content:
    p1, p2 = [x for x in content if x!=child] 
    if all(c in [a,b] for a,b,c in zip(p1,p2,child)):
        sim1 = sum(x == y for x,y in zip(p1, child))                
        sim2 = sum(x == y for x,y in zip(p2, child))                
        res += sim1*sim2
        break
print(res)