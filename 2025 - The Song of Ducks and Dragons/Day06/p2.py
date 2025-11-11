import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read()

mentor = {k: 0 for k in 'ABC'}
res = 0
for c in content:
    if c in mentor:
        mentor[c] += 1
    else:
        res += mentor[c.upper()]

print(res)