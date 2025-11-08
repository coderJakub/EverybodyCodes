import sys
from functools import cmp_to_key

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
    
    def GetScore(self):
        parts = [str(i) for i in [self.left, self.middle, self.right] if i is not None]
        return int("".join(parts))

class Sword:
    def __init__(self, id, fishbone):
        self.id = id
        self.fishbone = fishbone
    
    def GetQuality(self) -> int:
        return int("".join(str(x.middle) for x in self.fishbone))


def Compare(sword1, sword2) -> int:
    quality1 = sword1.GetQuality()
    quality2 = sword2.GetQuality()

    if quality1 != quality2:
        return 1 if quality1 < quality2 else -1
    
    for a,b in zip(sword1.fishbone, sword2.fishbone):
        if a.GetScore() != b.GetScore():
            return 1 if a.GetScore() < b.GetScore() else -1
    
    if len(sword1.fishbone) != len(sword2.fishbone):
        return 1 if len(sword1.fishbone) < len(sword2.fishbone) else -1
    
    return 1 if sword1.id < sword2.id else -1

swords = []
for line in content.splitlines():
    id = int(line.split(':')[0])
    nums = [int(x) for x in line.split(':')[1].split(',')]

    fishbones = [Fishbone(nums[0])]
    for el in nums[1:]:
        added = False
        for fb in fishbones:
            if fb.Add(el):
                added = True
                break
        if not added:
            fishbones.append(Fishbone(el))

    swords.append(Sword(id, fishbones))

res = 0
for i, sword in enumerate(sorted(swords, key=cmp_to_key(Compare))):
    res += (1+i)*sword.id

print(res)