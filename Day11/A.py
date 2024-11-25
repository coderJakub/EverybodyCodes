input = '''E:O,A
Y:E,O,I
A:U,Y
O:Y,A
I:U,Y,U
U:I,I,Y'''

pop = [line.split(':')[0] for line in input.splitlines()]
newPop = [line.split(':')[1].split(',') for line in input.splitlines()]

print(pop)
print(newPop)

population = ['A']
for i in range(4):
    newPopulation = []
    for p in population:
        for i in newPop[pop.index(p)]:
            newPopulation.append(i)
    population = newPopulation.copy()
    print(population)
    
print(len(population))