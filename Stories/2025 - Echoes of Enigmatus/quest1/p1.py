with open('in.txt', 'r') as file:
    lines = file.read().splitlines()
    
def eni(N, EXP, MOD):
    k = 1
    res = ""
    N, EXP, MOD = int(N[2:]), int(EXP[2:]), int(MOD[2:])
    for _ in range(EXP):
        k *= N
        k %= MOD
        res = str(k) + res
    return int(res)

h = 0
for line in lines:
    parts = line.split(' ')
    res = sum(eni(parts[i], parts[i + 3], parts[-1]) for i in range(3))
    h = max(h, res)

print(h)