#! /usr/bin/env python3

from pathlib import Path
from collections import Counter
from itertools import permutations

def boxIDdt(boxID):
    letter_freq = Counter(boxID)

    doubles = 0
    triples = 0

    for value in letter_freq.values():
        if   value == 2:
            doubles = 1
        elif value == 3:
            triples = 1

    return doubles, triples

def part1():
    with open(str(Path('../data/02.dat')), 'r') as f:
        data = [boxIDdt(line.strip()) for line in f]

    doubles = [dt[0] for dt in data]
    triples = [dt[1] for dt in data]

    return sum(doubles) * sum(triples)

def hamming_dist(s1, s2):
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def common_str(s1, s2):
    return ''.join(c1 for c1, c2 in zip(s1, s2) if c1 == c2)

def part2():
    with open(str(Path('../data/02.dat')), 'r') as f:
        data = [line.strip() for line in f]

    for boxID1, boxID2 in permutations(data,2):
       if hamming_dist(boxID1, boxID2) == 1:
           # print(boxID1)
           # print(boxID2)
           return common_str(boxID1, boxID2)

if __name__ == '__main__':

    # print(letter_duplicates("abcdef"))
    # print(letter_duplicates("ababab"))
    print(part1())

    # print(hamming_dist('1111','0000'))

    print(part2())
