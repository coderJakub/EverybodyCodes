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
    # A Cycle has been definitively found beacause EXP >> MOD
    resultIdx = (EXP-iterations-1)%len(found)
    repeatCount = (EXP-iterations-1)//(len(found) - breakpoint) 
    return sum(found[:breakpoint]) + sum(found[breakpoint:]) * (repeatCount + 1) + sum(found[breakpoint:resultIdx+1])

h = 0
for line in lines:
    parts = line.split(' ')
    res = sum(eni(parts[i], parts[i + 3], parts[-1]) for i in range(3))
    h = max(h, res)

print(h)