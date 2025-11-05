import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read().split(',')

data = set([int(x) for x in content])
print(sum(data))