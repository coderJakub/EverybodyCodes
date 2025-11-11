import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read()

mentor = 0
res = 0
for c in content:
    if c=='A':
        mentor += 1
    elif c=='a':
        res += mentor

print(res)