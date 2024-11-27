from itertools import permutations
with open('in.txt') as f:
    content = f.read().splitlines()

stars = []
for i,line in enumerate(content):
    for j,c in enumerate(line):
        if c == '*':
            stars.append([i,j])

solution = float('inf')
for perm in permutations(stars):
    reststars = []
    for i in perm:
        reststars.append(i)
    sum = 0
    for i,star in enumerate(perm[:-1]):
        reststars.pop(0)
        minA = float('inf')
        for starsR in reststars:
            a = abs(star[0]-starsR[0])+abs(star[1]-starsR[1])
            minA = min(minA,a)
        sum += minA
    solution = min(sum, solution)
    
    print(solution+len(stars))
print(len(stars))