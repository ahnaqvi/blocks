from Block import Block
import numpy

total_levels = 3
height = 1


def calculateWeights(weights, total_levels, blocks): # really the normal force
    blocks_reverse_sorted = list(reversed(sorted(blocks, key = lambda block: (block.y, block.x))))
    for block in blocks_reverse_sorted:
        if block.y == total_levels -1:
            weights[block] = 1
        else:
            # weight = weight of each neighbor * len of contact with neighbor
            weights[block] = 1 + sum([weights[i] * (1-abs(block.x - i.x)) for i in block.neighbors])
    
def checkStability(blocks):
    # blocks_dict = dict()
    # for block in blocks:
    #     if not blocks_dict[blocks.y]:
    #         blocks_dict[blocks.y] = {}
    #     blocks_dict[block.y].update({block.x: block})
    weights = {}
    [weights.update({block: -1}) for block in blocks] # weight exerted down by a block
    calculateWeights(weights, total_levels, blocks)
    
    



checkStability([Block(1,1),Block(1,2),Block(1,3)])