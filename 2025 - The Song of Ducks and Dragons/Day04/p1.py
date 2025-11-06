import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read().splitlines()
    
data = [int(x) for x in content]

res = 1
for i, el in enumerate(data[1:], start=1):
    before = data[i - 1]
    res *= before / el

print(int(res*2025))