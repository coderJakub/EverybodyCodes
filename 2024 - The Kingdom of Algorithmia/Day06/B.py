with open('in.txt') as f:
    input = f.read()

keys = [lines.split(':')[0] for lines in input.splitlines()]
values = [lines.split(':')[1].split(',') for lines in input.splitlines()]
d = dict(zip(keys, values))

def bfs(tree, start):
    queue = [[start, [start]]]
    paths = []
    while queue:
        node,path = queue.pop(0)
        if '@' ==node:
            paths.append(path)
            continue
        if node not in tree.keys():
            continue
        for neighbor in tree[node]:
            queue.append([neighbor, path + [neighbor]]) 
    return paths       

str = ''
paths = bfs(d, 'RR')
lenghts = [len(path) for path in paths]
for i,lenght in enumerate(lenghts):
    if lenghts.count(lenght) == 1:
        path = paths[i]
        break
for node in path:
    str += node[0]
print(str)