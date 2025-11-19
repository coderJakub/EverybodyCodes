import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read().splitlines()
    

wheel = [(1,1,1)]
wheel2 = []
totalLen = 1
for i, el in enumerate(content):
    a,b = list(map(int, el.split('-')))
    length = b-a+1
    totalLen += length
    if i%2==0:
        wheel.append((a,1,length))
    else:
        wheel2.append((b,-1,length))

wheel.extend(wheel2[::-1])
totalLen = 20252025%totalLen
for i, (a, fac, length) in enumerate(wheel):
    if totalLen < length:
        print(a+fac*totalLen)
        break
    totalLen -= length