import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read().splitlines()
    
res = 1
lastVal = int(content[0])
for i, el in enumerate(content[1:-1], start=1):
    g1, g2 = [int(x) for x in el.split('|')]
    res *= lastVal / g1
    lastVal = g2

res *= lastVal / int(content[-1])
print(int(res*100))