from typing import List, Tuple, Dict
import re

class WireGrid():
    def __init__(self):
        self.grid = dict()
        self.wirecount = 0

    def addwireinstructions(self, instructions: List[str]) -> None:
        x = 0
        y = 0
        length = 0
        self.addwirenode(x, y, length)
        for i in instructions:
            m = re.match(r"(\w)(\d+)", i)
            if m.group(1) == 'U':
                for _ in range(int(m.group(2))):
                    y += 1
                    length += 1
                    self.addwirenode(x,y, length)
            elif m.group(1) == 'D':
                for _ in range(int(m.group(2))):
                    y -= 1
                    length += 1
                    self.addwirenode(x,y, length)
            elif m.group(1) == 'R':
                for _ in range(int(m.group(2))):
                    x += 1
                    length += 1
                    self.addwirenode(x,y, length)
            elif m.group(1) == 'L':
                for _ in range(int(m.group(2))):
                    x -= 1
                    length += 1
                    self.addwirenode(x,y, length)
        self.wirecount += 1

    def addwirenode(self, x: int, y: int, length: int):
        self.grid.setdefault((x, y), dict())
        self.grid[(x, y)].setdefault(self.wirecount, length)

    def getintersections(self) -> List[Tuple[int, int]]:
        return [(k,v) for k, v in self.grid.items() if (len(v.keys()) > 1 and k != (0,0))]

def getminimummanhatten(intersections: List[Tuple[Tuple[int, int], Dict[int, int]]]) -> int:
    return min([abs(x[0][0]) + abs(x[0][1]) for x in intersections])

def getminimumsteps(intersections: List[Tuple[Tuple[int, int], Dict[int, int]]]):
    return min([sum(x[1].values()) for x in intersections])
