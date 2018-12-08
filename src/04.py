#! /usr/bin/env python3

from pathlib import Path
from itertools import groupby
from collections import Counter
import re

# is it worth using the datetime module instead to do this?
def parse(unsorted_records):
    for line in sorted(unsorted_records):
        (datetime, message) = re.match(r'\[(.*)\] (.*)', line).groups()
        if   message.startswith('Guard'):
            guard = int(message.split()[1][1:])
        elif message == 'falls asleep':
            sleep_time = int(datetime[-2:])
        elif message == 'wakes up':
            wake_time = int(datetime[-2:])
            yield (guard, sleep_time, wake_time)

def part1():
    pass

def part2():
    pass

if __name__ == '__main__':

    # print(part1())
    with open(str(Path('../data/04.dat')), 'r') as f:
        data = parse(f)

        # print(sorted(data, key=lambda gsw: gsw[0]))

        test = {k: [minute for (_, sleep_time, wake_time) in g
                    for minute in range(sleep_time, wake_time)]
                for (k, g) in groupby(sorted(data, key=lambda gsw: gsw[0]), lambda gsw: gsw[0])}

        guard, minutes = max(test.items(), key=lambda gt: len(gt[1]))

        print(guard) #863
        print(Counter(minutes).most_common(1)) #46

        times = {k: Counter(minutes).most_common(1)[0] for (k, minutes) in test.items()}
        guard = max(times, key=lambda k: times[k][1])

        print(guard) #373
        print(times[guard]) #40
