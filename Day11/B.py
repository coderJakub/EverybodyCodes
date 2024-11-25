input = '''C:M,Q,X
Z:R,K,F
Q:P,M,V,R
D:Q,Z,Z,P
R:Z,Q,V
S:B,M,G,M
M:G,X,Z
F:P,V,P,W
V:P,D,L
W:X,Q,D,L
B:R,D,M,N
G:N,P,J
K:H,C,G
P:S,C,F
N:L,D,P,V
X:H,V,T,D
T:B,P,C,B
L:D,B,Z
J:N,Z,T
H:W,C,B,D'''

pop = [line.split(':')[0] for line in input.splitlines()]
newPop = [line.split(':')[1].split(',') for line in input.splitlines()]

population = ['Z']
for i in range(10):
    newPopulation = []
    for p in population:
        for i in newPop[pop.index(p)]:
            newPopulation.append(i)
    population = newPopulation.copy()
    
print(len(population))