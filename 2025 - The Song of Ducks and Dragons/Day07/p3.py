import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read()
    
names = content.split('\n\n')[0].split(',')
instructions = content.split('\n\n')[1].splitlines()

insDict = {}
for instruction in instructions:
    left, right = instruction.split(' > ')
    insDict[left] = right.split(',')

filteredNames = []
for name in names:
    valid = True
    for i, char in enumerate(name[:-1]):
        if char not in insDict or name[i+1] not in insDict[char]:
            valid = False
            break
    if valid:
        filteredNames.append(name)

uniqueNames = set()
for name in filteredNames:
    names = [name]
    while len(names[0]) <= 11:
        newNames = []
        for fullname in names:
            if len(fullname) >= 7:
                uniqueNames.add(fullname)
            
            lastChar = fullname[-1]
            if lastChar in insDict:
                newNames.extend(fullname + char for char in insDict[lastChar])
        names = newNames

print(len(uniqueNames))