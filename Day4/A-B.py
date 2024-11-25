with open('in.txt') as f:
    lines = f.read().splitlines()

content = [int(line) for line in lines]

m = min(content)

count = 0
for nail in content:
    count += nail - m
print(count)