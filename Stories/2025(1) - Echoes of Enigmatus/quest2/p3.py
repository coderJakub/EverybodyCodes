from __future__ import annotations
from copy import deepcopy

with open("in.txt", "r") as file:
    data = file.read().split('\n')

class Direction:
    LEFT = 0
    RIGHT = 1

class Node:
    def __init__(self, rank, symbol):
        self.rank: int = rank #unique identifier for the node
        self.symbol: str = symbol #symbol of the node
        self.children: tuple[Node, Node] = (None, None)
    
    def rankIn(self, candidate: Node):
        if self.rank > candidate.rank:
            if self.children[Direction.LEFT] is None:
                self.children = (candidate, self.children[Direction.RIGHT])
            else:
                self.children[Direction.LEFT].rankIn(candidate)
        else:
            if self.children[Direction.RIGHT] is None:
                self.children = (self.children[Direction.LEFT], candidate)
            else:
                self.children[Direction.RIGHT].rankIn(candidate)
    
    def getBiggestLevel(self) -> str:
        level = [self]
        result = ""
        while len(level)>0:
            if len(result) < len(level):
                result = "".join([node.symbol for node in level])
            newLevel = []
            for node in level:
                if node.children[Direction.LEFT] is not None:
                    newLevel.append(node.children[Direction.LEFT])
                if node.children[Direction.RIGHT] is not None:
                    newLevel.append(node.children[Direction.RIGHT])
            level = newLevel
        return result
    
    def replace(self, rank: int, symbol: str, children: tuple[Node, Node]):
        self.rank = rank
        self.symbol = symbol
        self.children = children

nodes: dict[int, tuple[Node, Node]] = {}
def getNodes(line: str) -> tuple[Node, Node]:
    parts = line.split()
    lr, ls = parts[2][5:][1:-1].split(",")
    rr, rs = parts[3][6:][1:-1].split(",")
    nodes[int(parts[1][3:])] = (Node(int(lr), ls), Node(int(rr), rs))
    return nodes[int(parts[1][3:])]

def swap(id: int):
    if id in nodes:
        left, right = nodes[id]
        tr, ts, tc = left.rank, left.symbol, left.children
        left.replace(right.rank, right.symbol, right.children)
        right.replace(tr, ts, tc)
        
leftTree, rightTree = getNodes(data[0])
for line in data[1:]:
    if line.startswith("SWAP"):
        swap(int(line.split()[1]))
        continue
    leftNode, rightNode = getNodes(line)
    leftTree.rankIn(leftNode)
    rightTree.rankIn(rightNode)
    
print(leftTree.getBiggestLevel()+rightTree.getBiggestLevel())