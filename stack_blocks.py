from Block import Block
import numpy
from collections import OrderedDict

total_levels = 3
height = 1


# make directed graph of blocks
# only vertical forces going "up" are counted
# gravitational force is also unit size


# class multiGraph:
#     '''create force graph from blocks'''
#     def __init__(self, blocks):
#         self.blocks = blocks # list of blocks
#         n = len(blocks)
#         # self.matrix = numpy.array([[0 for i in range(n)] for i in range(n)])
#         blocks = reverse(sorted(blocks, key = lambda block: (block.y, block.x)))


def calculateWeights(weights, blocks_dict, blocks): 
    # y_values = list(reversed(sorted(blocks_dict.values())))
    # for level, y in enumerate(y_values):
        # if len()
    for block in blocks:
        if weights[block] != -1: # weight already defined
            continue
        if len(block.neighbors) == 0:
            weights[block] = 1
        else:
            for i in neighbors:
                if weights[i] == -1:
                    weights[i] # TODO
                weights[block] += weights[i]
          
def checkStability(blocks):
    # upwardForce = [0 for block in blocks] # normal forces applied TO each block
    # weight = [1 for block in blocks] # update in backward order
    # for i, block in enumerate(blocks):
    #     # if no block on top: # make func called findNeighbors
    #     #     upwardForce[i] = 0
    #     for each bottom neighbor of block:
    #         upwardForce[i] = contactArea *
    # blocks_reverse = list(reversed(sorted(blocks, key = lambda block: (block.y, block.x))))
    blocks_dict = dict()
    for block in blocks:
        if not blocks_dict[blocks.y]:
            blocks_dict[blocks.y] = {}
        blocks_dict[block.y].update({block.x: block})
    # top_blocks = list(blocks_dict[total_levels-1].values())
    # unvisited_blocks = {}
    # [unvisited_blocks.update({block: False}) for block in blocks]
    weights = {}
    [weights.update({block: -1}) for block in blocks] # weight exerted down by a block
    weights = calculateWeights(weights, blocks_dict, blocks)
    



checkStability([Block(1,1),Block(1,2),Block(1,3)])