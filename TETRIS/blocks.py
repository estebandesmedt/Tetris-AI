from block import Block
from position import Position

class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1,1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2,1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1,2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1,1), Position(2, 1)]
        }
        self.move(0,3)

class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1,1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1,1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1,2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2,0), Position(2, 1)]
        }
        self.move(0,3)

class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1,2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2,2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2,2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2,1), Position(3, 1)]
        }
        self.move(-1,3)

class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1,0), Position(1, 1)]
        }
        self.move(0,4)

class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1,0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1,2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2,0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1,1), Position(2, 1)]
        }
        self.move(0,3)

class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1,1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1,2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1,2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1,1), Position(2, 1)]
        }
        self.move(0,3)

class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1,1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1,2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2,1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1,1), Position(2, 0)]
        }
        self.move(0,3)

class GreyBlock(Block):
    def __init__(self):
        super().__init__(id = 8)
        self.cells = {
            0: [Position(0, 1), Position(0,2), Position(0, 3), Position(0, 4), Position(0,5), Position(0, 6), Position(0, 7), Position(0, 8), Position(0, 9)],
            1: [Position(0, 0), Position(0,2), Position(0, 3), Position(0, 4), Position(0,5), Position(0, 6), Position(0, 7), Position(0, 8), Position(0, 9)],
            2: [Position(0, 0), Position(0,1), Position(0, 3), Position(0, 4), Position(0,5), Position(0, 6), Position(0, 7), Position(0, 8), Position(0, 9)],
            3: [Position(0, 0), Position(0,1), Position(0, 2), Position(0, 4), Position(0,5), Position(0, 6), Position(0, 7), Position(0, 8), Position(0, 9)],
            4: [Position(0, 0), Position(0,1), Position(0, 2), Position(0, 3), Position(0,5), Position(0, 6), Position(0, 7), Position(0, 8), Position(0, 9)],
            5: [Position(0, 0), Position(0,1), Position(0, 2), Position(0, 3), Position(0, 4), Position(0, 6), Position(0, 7), Position(0, 8), Position(0, 9)],
            6: [Position(0, 0), Position(0,1), Position(0, 2), Position(0, 3), Position(0, 4), Position(0, 5), Position(0, 7), Position(0, 8), Position(0, 9)],
            7: [Position(0, 0), Position(0,1), Position(0, 2), Position(0, 3), Position(0, 4), Position(0, 5), Position(0, 6), Position(0, 8), Position(0, 9)],
            8: [Position(0, 0), Position(0,1), Position(0, 2), Position(0, 3), Position(0, 4), Position(0, 5), Position(0, 6), Position(0, 7), Position(0, 9)],
            9: [Position(0, 0), Position(0,1), Position(0, 2), Position(0, 3), Position(0, 4), Position(0, 5), Position(0, 6), Position(0, 7), Position(0, 8)]
        }
        self.move(0,0)