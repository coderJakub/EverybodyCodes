with open("in.txt", "r") as file:
    data = file.read().split('\n')
    
snails = []
for line in data:
    x,y = line.split()
    snails.append((int(x[2:]), int(y[2:])))

for _ in range(100):
    for i,snail in enumerate(snails):
        x,y = snail
        x+=1
        y-=1
        if y==0:
            y = x-1
            x = 1
        snail = (x, y)
        snails[i] = snail
    
score = 0
for snail in snails:
    x,y = snail
    score += x + y*100
print(score)