import sys
from collections import defaultdict

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read().split(',')
    
data = [int(x) for x in content]
countMap = defaultdict(int)
for num in data:
    countMap[num] += 1

print(max(countMap.values()))