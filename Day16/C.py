#import kleinstes gemeinsames Vielfaches
from math import gcd # gcd(x,y) = größter gemeinsamer Teiler von x und y -> kgV(x,y) = x*y/gcd(x,y)

with open('in.txt') as f:
    lines = f.read().splitlines()
    
leverAdj = [int(lever) for lever in lines[0].split(',')]
lines.pop(0)
lines.pop(0)

def getChars(string):
    s = set()
    for c in string:
        s.add(c)
    return s

spinners = [[] for _ in range(len(lines[0].split(' ')))]
for line in lines:
    j=0
    for i in range(len(spinners)):
        if not ' ' in list(line[j:j+3]) and not '' == line[j:j+3]:
            spinners[i].append(line[j:j+3])
        j+=4

# finde kleinstes gemeinsames Vielfaches von den Längen der einzelnen Spinnen
kgv = 1
for spinner in spinners:
    kgv = kgv * len(spinner) // gcd(kgv, len(spinner))

# Schritte bis zum kleinsten gemeinsamen Vielfachen
sum=0
for i in range(kgv):
    for j, lever in enumerate(leverAdj):
        for k in range(lever):
            spinners[j] = [spinners[j][1]] + spinners[j][2:] + [spinners[j][0]]
    str = ''
    for spinner in spinners:
        str += spinner[0][:1] + spinner[0][2:]
    for c in getChars(str):
        if str.count(c) >= 3:
            sum += str.count(c)-2
            
# Wiederholung der Schritte bis Restanzahl der Schritte erreicht
sum *= 202420242024//kgv

# Restliche Schritte
for i in range(202420242024%kgv):
    for j, lever in enumerate(leverAdj):
        for k in range(lever):
            spinners[j] = [spinners[j][1]] + spinners[j][2:] + [spinners[j][0]]
    str = ''
    for spinner in spinners:
        str += spinner[0][:1] + spinner[0][2:]
    for c in getChars(str):
        if str.count(c) >= 3:
            sum += str.count(c)-2

print(sum)