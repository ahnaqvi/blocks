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
            # weight = weight of each top neighbor * len of contact with neighbor
            weights[block] = 1 + sum([weights[i] * (1-abs(block.x - i.x)) for i in block.neighbors if i.y > block.y])

def halfway_point(block, neighbor):
    return (min(block.x, neighbor.x) + 1 - max(block.x, neighbor.x))/2
    
def checkStability(blocks):
    # blocks_dict = dict()
    # for block in blocks:
    #     if not blocks_dict[blocks.y]:
    #         blocks_dict[blocks.y] = {}
    #     blocks_dict[block.y].update({block.x: block})
    weights = {}
    [weights.update({block: -1}) for block in blocks] # weight exerted down by a block
    calculateWeights(weights, total_levels, blocks)
    epsilon = 0.0005
    # balance forces and momentum
    print(weights.values())
    
    for block in blocks:
        for neighbor in block.neighbors:
            top_neighbors_weights = []
            bottom_neighbors_weights = []
            top_neighbors_momentums = []
            bottom_neighbors_momentums = []
            if block.y == 0: # consider the table as a neighbor
                contact_distance = min(block.x + 1, 0) - block.x
                halfway_point_i = contact_distance / 2
                bottom_neighbors_weights.append(weights[block] * abs(contact_distance))
                bottom_neighbors_momentums.append(weights[block] * abs(contact_distance) * halfway_point_i)
            for i in block.neighbors:
                halfway_point_i = halfway_point(block, i)
                contact_distance = (1-abs(block.x - i.x))
                if i.y < block.y:
                    bottom_neighbors_weights.append(weights[block] * contact_distance)
                    bottom_neighbors_momentums.append(weights[block]  * contact_distance * halfway_point_i)
                if i.y > block.y:
                    top_neighbors_weights.append(weights[i] * contact_distance)
                    top_neighbors_momentums.append(weights[i] * contact_distance * halfway_point_i)
            weight_diff = sum(bottom_neighbors_weights) - sum(top_neighbors_weights)
            momentum_diff = sum(bottom_neighbors_momentums) - sum(top_neighbors_momentums)
            print(bottom_neighbors_weights)
            assert(weight_diff <= 1 + epsilon and weight_diff >= 1-epsilon)
            assert(momentum_diff <= block.x + 0.5 + epsilon and momentum_diff >= block.x + 0.5 - epsilon)
            for i in weights.values():
                assert(i > 0)
            
        
        # bottom_neighbors_weight = sum([weights[block] * (1-abs(block.x - i.x)) for i in block.neighbors if i.y < block.y])
        # top_neighbors_weight = sum([weights[i] * (1-abs(block.x - i.x)) for i in block.neighbors if i.y > block.y])
        # weight_diff = bottom_neighbors_weight - top_neighbors_weight
        # assert( weight_diff <= 1 + epsilon and weight_diff >= 1-epsilon)
        
        # # halfway_points = [halfway_point(block, neighbor) for neighbor in block.neighbors]
        # top_neighbors_momentum = sum([ weights[block] * (1-abs(block.x - i.x)) * halfway_point(block, i) for i in block.neighbors if i.y > block.y])
        # bottom_neighbors_momentum = sum([ weights[block] * (1-abs(block.x - i.x)) * halfway_point(block, i) for i in block.neighbors if i.y < block.y])
        # momentum_diff = bottom_neighbors_momentum - top_neighbors_momentum
        # assert(momentum_diff <= block.x + 0.5 + epsilon and momentum_diff >= block.x + 0.5 - epsilon)
                
block1 = Block(-5/6, 0)
block2 = Block(-1+(1/4+1/6), 1)
block3 = Block(-1/12, 2)
block1.addNeighbor(block2)
block2.addNeighbor(block1)
block2.addNeighbor(block3)
block3.addNeighbor(block2)
checkStability([block1, block2, block3])