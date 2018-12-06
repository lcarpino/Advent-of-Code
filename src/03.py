#! /usr/bin/env python3

from pathlib import Path
from collections import namedtuple
from itertools import combinations

rectangle = namedtuple('rectangle', ['left', 'right', 'top', 'bottom'])

def parse_claim(claim):
    raw_id, _, raw_pos, raw_size = claim.split()

    # extract from claim
    id = int(raw_id[1:])
    left, top = map(int, raw_pos.strip(':').split(','))
    width, height = map(int, raw_size.split('x'))

    # compute boundaries of rectangle
    right = left + width
    bottom = top + height

    return id, rectangle(left, right, top, bottom)

def overlap(rect1, rect2):
    x_overlap = max(0, min(rect1.right, rect2.right) - max(rect1.left, rect2.left))
    y_overlap = max(0, min(rect1.bottom, rect2.bottom) - max(rect1.top, rect2.top))

    return x_overlap * y_overlap

def part1():
    with open(str(Path('../data/03.dat')), 'r') as f:
        data = [line.strip() for line in f]


    ## this approach results in double counting

    # rectangles = [rect for _, rect in
    #               [parse_claim(claim) for claim in data]]

    # overlap_regions = []
    # for rect1, rect2 in combinations(rectangles[0:100], 2):
    #     overlap_regions.append(overlap(rect1, rect2))

    # return overlap_regions

if __name__ == '__main__':

    # test cases...
    # id1, rect1 = parse_claim("#1 @ 1,3: 4x4")
    # id2, rect2 = parse_claim("#2 @ 3,1: 4x4")
    # id3, rect3 = parse_claim("#3 @ 5,5: 2x2")
    # print(overlap(rect1, rect2))
    # print(overlap(rect1, rect3))
    # print(overlap(rect2, rect3))

    print(part1())
