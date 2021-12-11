import numpy as np
import cv2


# https://adventofcode.com/2021/day/11


file = open('input.txt', 'r')
lines = file.readlines()
octopuses  = []
for line in lines:
    octopuses .append([int(char) for char in line.rstrip()])
octopuses  = np.asarray(octopuses, dtype=np.int16)

neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def update_flashes(octopuses, row, col):
    if row < 0 or col < 0 or row >= octopuses.shape[0] or col >= octopuses.shape[1]:
        return
        
     
    if octopuses[row,col] == 0:  # octupus already flashed once
        return

    octopuses[row,col] += 1
    
    if octopuses[row,col] > 9:
        # octupus flashes!
        octopuses[row,col] = 0
        for neighbor in neighbors:
            update_flashes(octopuses, row+neighbor[0], col+neighbor[1])


step = 0
num_steps = 100
total_flashes = 0
while True:
    octopuses += 1
    for row in range(octopuses.shape[0]):
        for col in range(octopuses.shape[1]):
            if octopuses[row,col] > 9:
                update_flashes(octopuses, row, col)
    num_flashes = (octopuses == 0).sum()
    total_flashes += num_flashes
    step += 1
    
    if step == num_steps:
        print('Result part 1: ', total_flashes)
        
    if num_flashes == 100:
        print('Result part 2: ', step)
        break
    