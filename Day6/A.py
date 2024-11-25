with open('in.txt') as f:
    input = f.read()

keys = [lines.split(':')[0] for lines in input.splitlines()]
values = [lines.split(':')[1].split(',') for lines in input.splitlines()]
d = dict(zip(keys, values))

