import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read()
    
    
def add(a, b):
    [a1, a2] = a
    [b1, b2] = b
    return [a1 + b1, a2 + b2]

def multiply(a, b):
    [a1, a2] = a
    [b1, b2] = b
    return [a1 * b1 - a2 * b2, a1 * b2 + a2 * b1]

def divide(a, b):
    [a1, a2] = a
    [b1, b2] = b
    return [a1 // b1, a2 // b2]

data = [int(x) for x in content.split("=")[1][1:-1].split(",")]
R = [0,0]

for i in range(3):
    R = multiply(R, R)
    R = divide(R, [10,10])
    R = add(R, data)

print(f"[{R[0]},{R[1]}]")