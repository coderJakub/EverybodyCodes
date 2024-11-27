from collections import defaultdict

with open('in.txt') as f:
    lines = f.read().splitlines()

p = []

for line in lines:
    k = line.split(':')[0]
    v = line.split(':')[1].split(',')

    value = 10
    sum = 0
    for i in range(10):
        match v[i%len(v)]:
            case '+': value += 1
            case '-': value -= 1
        sum += value
    p.append((k,sum))

p.sort(key=lambda x: x[1], reverse=True)
str =""
for i in p:
    str+=i[0]
print(str)