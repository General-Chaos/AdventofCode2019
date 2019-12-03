from typing import List, Tuple


class ShipComputer():

    def __init__(self, itr: List[int]):
        self.itr = itr

    def runprogram(self, noun: int = None, verb: int = None) -> List[int]:
        optidx = 0
        itr = self.itr.copy()
        if noun is not None:
            itr[1] = noun
        if verb is not None:
            itr[2] = verb
        opcode = itr[optidx]
        while(opcode != 99):
            if opcode == 1:
                itr[itr[optidx + 3]] = itr[itr[optidx + 1]] + \
                    itr[itr[optidx + 2]]
            elif opcode == 2:
                itr[itr[optidx + 3]] = itr[itr[optidx + 1]] * \
                    itr[itr[optidx + 2]]
            else:
                raise ValueError(f"Bad opcode: {opcode}")
            optidx += 4
            opcode = itr[optidx]
        return itr

    def getnounverb(self, desiredvalue: int, maxsearch: int) -> Tuple[int, int]:
        for i in range(maxsearch):
            for j in range(maxsearch):
                if self.runprogram(i, j)[0] == desiredvalue:
                    return (i, j)
        raise ValueError(
            f"Desired value {desiredvalue} not found in search range {maxsearch}")
