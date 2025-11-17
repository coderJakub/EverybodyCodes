import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = list(map(int, f.read().splitlines()))


phase1 = -1
changes = True
while changes:
    changes = False
    for i,(a,b) in enumerate(zip(content, content[1:])):
        if a > b:
            content[i] -= 1
            content[i+1] += 1
            changes = True
    phase1 += 1

avg = sum(content) // len(content)
phase2 = sum(abs(d-avg) for d in content) // 2
print(phase1+phase2)