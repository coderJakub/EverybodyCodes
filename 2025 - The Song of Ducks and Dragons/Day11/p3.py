import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = list(map(int, f.read().splitlines()))

# phase 1 finished beacause 1 < 2 < ... < n-1 < ... n
# -> strictly ascending

avg = sum(content) // len(content)
res = sum(abs(d-avg) for d in content) // 2

print(res)