import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read()*1000

res = 0
for i,c in enumerate(content):
    if c in 'abc':
        l = max(0, i-1000)
        r = min(len(content), i+1000)
        res += content[l:r+1].count(c.upper())

print(res)