with open('in.txt') as f:
    lines = f.read().splitlines()

content = [int(line) for line in lines]

count = [0 for _ in range(len(content))]
for i,m in enumerate(content):
    countS = 0
    for nail in content:
        countS += abs(nail - m)
    count[i] = countS
print(min(count))