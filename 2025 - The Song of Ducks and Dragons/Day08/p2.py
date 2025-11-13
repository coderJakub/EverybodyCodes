import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = list(map(int, f.read().split(',')))

res = 0
pairs = []
for a, b in zip(content, content[1:]):
    if b < a: a,b = b,a
    for (i,j) in pairs:
        if i < a < j < b or a < i < b < j:
            res += 1
    pairs.append((a, b))

print(res)