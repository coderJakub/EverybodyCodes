with open('in.txt') as f:
    content = f.read()

def getNeededBlocks(available, priest, nullpriest):
    bottomLayer = 1
    nextLayerSize = 1
    while True:
        
        if available <= nextLayerSize*bottomLayer:
            return (bottomLayer) * (nextLayerSize*bottomLayer - available)
        
        available -= nextLayerSize*bottomLayer
        bottomLayer += 2
        nextLayerSize = (nextLayerSize*nullpriest)%priest

print(getNeededBlocks(20240000, 1111, int(content)))