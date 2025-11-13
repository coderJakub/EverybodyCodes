import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = list(map(int, f.read().split(',')))
    
res = 0
for a, b in zip(content, content[1:]):
    if abs(a - b) == 32/2:
        res += 1
print(res)