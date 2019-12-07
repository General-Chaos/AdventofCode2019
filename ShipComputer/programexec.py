from typing import List, Tuple


class Program_Executor:

    def __init__(self, itr: List[int], inputs: List[int] = None):
        self.itr = itr.copy()
        self.inputs = inputs
        self.opidx = 0
        self.outputs = list()

    def runprogram(self):
        while self.itr[self.opidx] != 99:
            self._step()
        return {
            'itr': self.itr,
            'output': self.outputs
        }

    def _step(self):
        opcode = self._getopcodefunc()
        getattr(self, opcode)()

    def _getopcodefunc(self):
        return 'opcode_' + ''.join(str(self.itr[self.opidx]).zfill(2)[-2:])

    def _getparameters(self, count):
        masks = str(self.itr[self.opidx]).zfill(5)[-5:-2]
        masks = list(reversed([int(x) for x in masks]))
        params = list()
        for i in range(count):
            if masks[i]:
                params.append(self.itr[self.opidx + i + 1])
            else:
                params.append(self.itr[self.itr[self.opidx + i + 1]])
        return params

    def opcode_01(self):
        params = self._getparameters(2)
        self.itr[self.itr[self.opidx + 3]] = params[0] + params[1]
        self.opidx += 4

    def opcode_02(self):
        params = self._getparameters(2)
        self.itr[self.itr[self.opidx + 3]] = params[0] * params[1]
        self.opidx += 4

    def opcode_03(self):
        self.itr[self.itr[self.opidx + 1]] = self.inputs.pop(0)
        self.opidx += 2

    def opcode_04(self):
        params = self._getparameters(1)
        self.outputs.append(params[0])
        self.opidx += 2

    def opcode_05(self):
        params = self._getparameters(2)
        if params[0] != 0:
            self.opidx = params[1]
        else:
            self.opidx += 3

    def opcode_06(self):
        params = self._getparameters(2)
        if params[0] == 0:
            self.opidx = params[1]
        else:
            self.opidx += 3

    def opcode_07(self):
        params = self._getparameters(2)
        if params[0] < params[1]:
            result = 1
        else:
            result = 0
        self.itr[self.itr[self.opidx + 3]] = result
        self.opidx += 4

    def opcode_08(self):
        params = self._getparameters(2)
        if params[0] == params[1]:
            result = 1
        else:
            result = 0
        self.itr[self.itr[self.opidx + 3]] = result
        self.opidx += 4
