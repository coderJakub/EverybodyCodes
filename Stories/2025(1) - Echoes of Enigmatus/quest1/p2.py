with open('in.txt', 'r') as file:
    lines = file.read().splitlines()
    
def eni(N, EXP, MOD):
    k = 1
    found = []
    N, EXP, MOD = int(N[2:]), int(EXP[2:]), int(MOD[2:])
    iterations = 0
    for iterations in range(EXP):
        k *= N
        k %= MOD
        if k in found:
            breakpoint = found.index(k)
            break
        found.append(k)
    resultIdx = (EXP-iterations-1)%len(found)
    result = ""
    idx = resultIdx
    for _ in range(5):
        result += str(found[idx])
        idx -= 1
        if idx < breakpoint:
            idx = len(found) - 1
    return int(result)

h = 0
for line in lines:
    parts = line.split(' ')
    res = sum(eni(parts[i], parts[i + 3], parts[-1]) for i in range(3))
    h = max(h, res)

print(h)