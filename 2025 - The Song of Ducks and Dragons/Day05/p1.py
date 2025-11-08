import sys

fileName = sys.argv[1]
with open(fileName) as f:
    content = f.read()

class Fishbone:
    def __init__(self, num: int):
        self.middle = num
        self.left = None
        self.right = None
    
    def IsFull(self) -> bool:
        return all(x is not None for x in [self.left, self.middle, self.right])
    
    def Add(self, num: int) -> bool:
        if self.IsFull():
            return False
        
        if num < self.middle and not self.left:
            self.left = num
            return True
        if self.middle < num and not self.right:
            self.right = num
            return True
        return False

nums = [int(x) for x in content.split(':')[1].split(',')]

fishbones = [Fishbone(nums[0])]
for el in nums[1:]:
    added = False
    for fb in fishbones:
        if fb.Add(el):
            added = True
            break
    if not added:
        fishbones.append(Fishbone(el))

res = "".join(str(x.middle) for x in fishbones)

print(res)