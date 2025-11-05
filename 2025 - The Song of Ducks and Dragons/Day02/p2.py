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
    return [int(a1 / b1), int(a2 / b2)]

def cycle(point):
    k = [0, 0]
    for i in range(100):
        k = multiply(k, k)
        k = divide(k, [100000,100000])
        k = add(k, point)

        x, y = k
        if not (-1000000 <= x <= 1000000 and -1000000 <= y <= 1000000):
            return False
    return True

data = [int(x) for x in content.split("=")[1][1:-1].split(",")]

x = data[0]
y = data[1]

res = 0
for i in range(101):
    y = data[1]
    for j in range(101):
        if cycle([x,y]):
            res += 1
        y += 10
    x += 10

print(res)