import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = list(map(int, f.read().splitlines()))


round = -1
changes = True
while changes:
    changes = False
    for i,(a,b) in enumerate(zip(content, content[1:])):
        if a > b:
            content[i] -= 1
            content[i+1] += 1
            changes = True
    round += 1

while round < 10:
    round += 1
    for i,(a,b) in enumerate(zip(content, content[1:])):
        if a < b:
            content[i] += 1
            content[i+1] -= 1
res = sum(i*a for i, a in enumerate(content, start=1))
print(res)