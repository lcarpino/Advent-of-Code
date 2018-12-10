#! /usr/bin/env python3

from pathlib import Path
from itertools import takewhile
from collections import Counter

def parse(coord_list):
    coordinates = [[int(coord) for coord in coord_pair.split(', ')]
                   for coord_pair in coord_list]
    return coordinates

def coord_bounds(coordinates):
    x_coords, y_coords = zip(*coordinates)

    xmin = min(x_coords)
    xmax = max(x_coords)
    ymin = min(y_coords)
    ymax = max(y_coords)

    return xmin, xmax, ymin, ymax

def L1_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def part1(coordinates):

    xmin, xmax, ymin, ymax = coord_bounds(coordinates)
    atlas = {}

    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            # sort and iterate only over as many as share the minimum distance
            npoint_dists = sorted(((n, L1_dist((x,y), coord))
                                   for (n, coord) in enumerate(coordinates)),
                                  key=lambda x: x[1])
            closest = [*takewhile(lambda x: x[1] == npoint_dists[0][1], npoint_dists)]
            if len(closest) > 1:
                continue
            atlas[x, y] = closest[0][0]

    edges = {n for ((x, y), n) in atlas.items()
             if x in {xmin, xmax} or y in {ymin, ymax}}
    areas = Counter(n for n in atlas.values() if n not in edges)
    return areas.most_common(1)[0][1]

def part2(coordinates, max_tot_dist):

    xmin, xmax, ymin, ymax = coord_bounds(coordinates)
    atlas = {}

    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            dist = sum((L1_dist((x,y), coord)
                         for coord in coordinates))
            if dist >= max_tot_dist:
                continue
            atlas[x, y] = 1
    return sum(atlas.values())

if __name__ == '__main__':

    with open(str(Path('../data/06.dat')), 'r') as f:
        coordinates = parse(f)

    print(part1(coordinates))

    print(part2(coordinates, max_tot_dist=10000))
