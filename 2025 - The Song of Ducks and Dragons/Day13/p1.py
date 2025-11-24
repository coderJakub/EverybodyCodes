import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read().splitlines()
    

wheel = [1]
wheel2 = []
for i, el in enumerate(content):
    if i%2==0:
        wheel.append(el)
    else:
        wheel2.append(el)
    
wheel.extend(wheel2[::-1])
print(wheel[2025%len(wheel)])

# oder: print(([1]+[*content[::2]]+[*content[1::2][::-1]])[2025%(len(content)+1)])