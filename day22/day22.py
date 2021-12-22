# https://adventofcode.com/2021/day/22
import re
import numpy as np


file = open('input.txt', 'r')
ranges = []
# for line in file.readlines():
ranges_data = re.findall(r'([on|off]) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', file.read())
ranges = [(True, int(range[1]),int(range[2]),int(range[3]),int(range[4]),int(range[5]),int(range[6])) if range[0] == 'n' else (False, int(range[1]),int(range[2]),int(range[3]),int(range[4]),int(range[5]),int(range[6])) for range in ranges_data]


def part1():
    core = np.zeros((101,101,101), dtype=np.bool_)
    for range in ranges:
        minX = max(range[1]+50, 0)
        maxX = min(range[2]+1+50, core.shape[0])
        minY = max(range[3]+50, 0)
        maxY = min(range[4]+1+50, core.shape[1])
        minZ = max(range[5]+50, 0)
        maxZ = min(range[6]+1+50, core.shape[2])
        core[minX:maxX,minY:maxY,minZ:maxZ] = range[0]
        #print("%d:%d, %d:%d, %d:%d"%(minX,maxX,minY,maxY,minZ,maxZ), range[0])
    return core.sum()


print('Result part 1: ', part1())


# part 2
# use window sliding, slide blocks over input and count per block (ideally reusing part 1)

