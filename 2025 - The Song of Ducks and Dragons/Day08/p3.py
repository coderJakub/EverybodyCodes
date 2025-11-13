import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = list(map(int, f.read().split(',')))

res = 0
pairs = []
for a, b in zip(content, content[1:]):
    if b < a: a,b = b,a
    pairs.append((a, b))

maxCut = 0
for i in range(1, 257):
    for j in range(i+1, 257):
        cuts = 0
        for a,b in pairs:
            if i < a < j < b or a < i < b < j:
                cuts += 1
        maxCut = max(maxCut, cuts)
print(maxCut)