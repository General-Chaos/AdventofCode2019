from .programexec import Program_Executor
from typing import List, Tuple


class ShipComputer():

    def __init__(self, itr: List[int]):
        self.itr = itr

    def runprogram(self, noun: int = None, verb: int = None, inputs: List[int] = None):
        itr = self.itr.copy()
        if noun is not None:
            itr[1] = noun
        if verb is not None:
            itr[2] = verb
        program = Program_Executor(itr, inputs=inputs)
        return program.runprogram()
