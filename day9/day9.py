import numpy as np
import cv2


# https://adventofcode.com/2021/day/9



file = open('input.txt', 'r')
lines = file.readlines()
heightmap = []
for line in lines:
    heightmap.append([int(char) for char in line.rstrip()])

heightmap = np.asarray(heightmap, dtype=np.int16)

neighbors = [(-1,0),(1,0),(0,-1),(0,1)]

low_points = []
for row in range(heightmap.shape[0]):
    for col in range(heightmap.shape[1]):
        local_min = True
        for neighbor in neighbors:
            new_row = row + neighbor[0]
            new_col = col + neighbor[1]
            if new_row < 0 or new_row >= heightmap.shape[0] or new_col < 0 or new_col >= heightmap.shape[1]:
                continue
            elif heightmap[new_row, new_col] <= heightmap[row, col]:
                local_min = False
                break
        if local_min is True:
            # low point found
            low_points.append((row, col))
        
print('Result part 1: ', sum([heightmap[row, col] +1 for (row, col) in low_points]))


bassins = np.copy(heightmap)
bassins[bassins<9] = 255
bassins[bassins==9] = 0
bassins = bassins.astype('uint8')
retval, labels, stats, centroids = cv2.connectedComponentsWithStatsWithAlgorithm(bassins, connectivity=4, ltype=cv2.CV_32S, ccltype=cv2.CCL_DEFAULT)
areas = sorted(stats[1:,4], reverse=True) # ignore the first connected component since it is the background layer
print('Result part 2: ', areas[0]*areas[1]*areas[2])
