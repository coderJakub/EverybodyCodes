with open('in.txt') as f:
    content = f.read()

def getNeededBlocks(available, priestac, highpriest):
    layers = 0
    nextLayerSize = 1
    columnHeight =[]
    while True:
        for i in range(layers):
            columnHeight[i] += nextLayerSize
        columnHeight.append(nextLayerSize)
        layers += 1
        w = layers*2-1
        
        removed = 0
        needed = sum(columnHeight)*2-columnHeight[0]
        for i,column in enumerate(columnHeight[:-1]):
            add = ((highpriest*w)*column % priestac)
            if i!=0:
                add*=2
            removed += add
        needed -= removed
        
        if available <= needed:
            return needed - available
        
        nextLayerSize = (nextLayerSize*highpriest)%priestac+priestac

print(getNeededBlocks(202400000, 10, int(content)))