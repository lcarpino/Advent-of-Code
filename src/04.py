#! /usr/bin/env python3

from pathlib import Path
from collections import namedtuple
import re

def parse(lines):
    for line in sorted(lines):
        (time, message) = re.match(r'\[(.*)\] (.*)', line).groups()
        print(time, message)

def part1():
    pass

def part2():
    pass

if __name__ == '__main__':

    # print(part1())
     with open(str(Path('../data/04.dat')), 'r') as f:
         parse(f)
