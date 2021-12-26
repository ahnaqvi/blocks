class Block:
    # width = 1
    # height = 1
    # weight = 1
    def __init__(self, x, y): # x is left bottom position of block wr to table. table extends to (0,0)
        self.x = x
        self.y = y
        self.neighbors = []
    def addNeighbor(self, block): # only top and bottom neighbors are important
        self.neighbors.append(block)

