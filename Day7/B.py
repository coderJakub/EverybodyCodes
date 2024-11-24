from collections import defaultdict

with open('in.txt') as f:
    lines = f.read().splitlines()

with open('track.txt') as f:
    linesT = f.read().splitlines()

track =""
for c in linesT[0]:
    track+=c
for i in range(1,len(linesT)-1):
    track+=linesT[i][-1]
for c in reversed(linesT[-1]):
    track+=c
for i in reversed(range(1,len(linesT)-1)):
    track+=linesT[i][0]
track = track[1:] + '='
p = []

for line in lines:
    k = line.split(':')[0]
    v = line.split(':')[1].split(',')

    value = 10
    sum = 0
    j = 0
    for i in range(10):
        for c in track:
            match c:
                case '+': value += 1
                case '-': value -= 1
                case '=':
                    match v[j%len(v)]:
                        case '+': value += 1
                        case '-': value -= 1
            j+=1
            sum += value
    p.append((k,sum))

p.sort(key=lambda x: x[1], reverse=True)
str =""
for i in p:
    str+=i[0]
print(str)