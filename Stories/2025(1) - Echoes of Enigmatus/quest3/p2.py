import gmpy2
with open("in.txt", "r") as file:
    data = file.read().split('\n')
    
snails = []
for line in data:
    x,y = line.split()
    x = int(x[2:])
    y = int(y[2:])
    toBottom = y-1
    iterations = x+y-1
    snails.append((toBottom, iterations))

# Löse lineare Kongruenz: x ≡ a mod m UND x ≡ b mod n
def getCombined(a1, m1, a2, m2):
    d, x1, _ = gmpy2.gcdext(m1, m2)
    lcm = m1 * m2 // d
    x = (a1 + (a2 - a1) // d * x1 * m1) % lcm
    return (x, lcm)

ah,kh = snails[0]
for a,k in snails[1:]:
    ah,kh = getCombined(ah, kh, a, k)

print(ah)