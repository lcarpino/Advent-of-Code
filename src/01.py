#! /usr/bin/env python3

from pathlib import Path
from itertools import cycle

def part1():
    with open(str(Path('./data/01.dat')), 'r') as f:
        data = [int(line.strip()) for line in f]

    return sum(data)

def part2():
    with open(str(Path('./data/01.dat')), 'r') as f:
        data = [int(line.strip()) for line in f]

    data_repeater = cycle(data)

    freq_start = 0

    freq = freq_start
    freq_list = set([0])

    for dfreq in data_repeater:
        freq = freq + dfreq

        if freq in freq_list:
            return freq

        freq_list.add(freq)

if __name__ == '__main__':

    print(part1())

    print(part2())
