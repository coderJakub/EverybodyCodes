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

for name in names:
    valid = True
    for i, char in enumerate(name[:-1]):
        if char not in insDict or name[i+1] not in insDict[char]:
            valid = False
            break
    if valid:
        print(name)
        break        