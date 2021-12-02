import numpy as np

# https://adventofcode.com/2021/day/2


# part 1
with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    
hor, vert, depth = 0, 0, 0
for line in lines:
    (dir, count) = line.split(' ')
    count = int(count)
    if dir=='forward':
        hor += count
    if dir=='down':
        depth += count
    if dir=='up':
        depth -= count
        
print('Result part 1: ', hor * depth)

    
# part 2
hor, vert, depth, aim = 0, 0, 0, 0
for line in lines:
    (dir, count) = line.split(' ')
    count = int(count)
    if dir=='forward':
        hor += count
        depth += (aim * count)
    if dir=='down':
        aim += count
    if dir=='up':
        aim -= count
        
print('Result part 2: ', hor * depth)

    
