#! /usr/bin/env python3

from pathlib import Path
from collections import namedtuple, defaultdict
from itertools import combinations
from functools import reduce

# rectangle = namedtuple('rectangle', ['left', 'right', 'top', 'bottom'])
claim = namedtuple('claim', ['id', 'left', 'top', 'width', 'height'])

def parse_claim(claim_text):
    raw_id, _, raw_pos, raw_size = claim_text.split()

    # extract from claim
    id = int(raw_id[1:])
    left, top = map(int, raw_pos.strip(':').split(','))
    width, height = map(int, raw_size.split('x'))

    # compute boundaries of rectangle
    # right = left + width
    # bottom = top + height

    return claim(id, left, top, width, height)

# def overlap(rect1, rect2):
#     x_overlap = max(0, min(rect1.right, rect2.right) - max(rect1.left, rect2.left))
#     y_overlap = max(0, min(rect1.bottom, rect2.bottom) - max(rect1.top, rect2.top))

#     return x_overlap * y_overlap

def part1():
    with open(str(Path('../data/03.dat')), 'r') as f:
        data = [line.strip() for line in f]

    claims = [claim for claim in
                  [parse_claim(claim) for claim in data]]

    grid = defaultdict(int)

    for claim in claims:
        for x in range(claim.left, claim.left + claim.width):
            for y in range(claim.top, claim.top + claim.height):
                grid[x, y] += 1

    overlap = 0

    for keys, value in grid.items():
        if value > 1:
            overlap += 1

    return overlap

    ## this approach results in double counting

    # rectangles = [rect for _, rect in
    #               [parse_claim(claim) for claim in data]]

    # overlap_regions = []
    # for rect1, rect2 in combinations(rectangles[0:100], 2):
    #     overlap_regions.append(overlap(rect1, rect2))

    # return overlap_regions

def part2():
    with open(str(Path('../data/03.dat')), 'r') as f:
        data = [line.strip() for line in f]

    claims = [claim for claim in
                  [parse_claim(claim) for claim in data]]

    grid = defaultdict(int)

    for claim in claims:
        for x in range(claim.left, claim.left + claim.width):
            for y in range(claim.top, claim.top + claim.height):
                grid[x, y] += 1

    for claim in claims:
        if all(grid[x, y] == 1
               for x in range(claim.left, claim.left + claim.width)
               for y in range(claim.top, claim.top + claim.height)):
            return claim.id

if __name__ == '__main__':

    # test cases...
    # id1, rect1 = parse_claim("#1 @ 1,3: 4x4")
    # id2, rect2 = parse_claim("#2 @ 3,1: 4x4")
    # id3, rect3 = parse_claim("#3 @ 5,5: 2x2")
    # print(overlap(rect1, rect2))
    # print(overlap(rect1, rect3))
    # print(overlap(rect2, rect3))

    print(part1())

    print(part2())
