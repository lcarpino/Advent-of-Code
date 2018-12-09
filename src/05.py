#! /usr/bin/env python3

from pathlib import Path
from functools import reduce

def parse(polymer):
    for line in polymer:
        return line.strip()

def polymer_reducer(base_chain, new_base):
    # if   base_chain and base_chain[-1] != new_base and base_chain[-1].upper() == new_base.upper():
    if   base_chain and base_chain[-1] == new_base.swapcase():
        base = base_chain[:-1]
    else:
        base = base_chain + new_base
    return base

def polymerase(polymer):
    return reduce(polymer_reducer, polymer)

def part1(polymer):
    return len(polymerase(polymer))

def part2(polymer):
    return min(
        (len(polymerase(polymer.replace(base, '').replace(base.upper(), '')))
                for base in 'abcdefghijklmnopqrstuvwxyz'))

if __name__ == '__main__':

    with open(str(Path('../data/05.dat')), 'r') as f:
        data = parse(f)

        print(part1(data))
        print(part2(data))
