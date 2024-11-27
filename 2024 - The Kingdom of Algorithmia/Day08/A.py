with open('in.txt') as f:
    content = f.read()

def getNeededBlocks(available):
    nextLayerSize = 1
    while True:
        if available <= nextLayerSize:
            return (nextLayerSize) * (nextLayerSize - available)
        
        available -= nextLayerSize
        nextLayerSize += 2
        
print(getNeededBlocks(int(content)))