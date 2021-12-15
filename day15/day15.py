import numpy as np
import sys
from queue import PriorityQueue

# https://adventofcode.com/2021/day/15


file = open('input.txt', 'r')
cave = np.asarray([list(line.rstrip()) for line in file.readlines()], dtype=np.int16)

neighbors = [(-1,0),(0,-1), (0,1),(1,0)]


def find_path_dijkstra(cave):
    queue = PriorityQueue()
    queue.put((0,(0,0)))
    cost_matrix = np.ones(cave.shape, dtype=np.int16) * sys.maxsize
    cost_matrix[0,0] = 0
    
    visited = np.zeros(cave.shape, dtype=np.int16)
    
    while not queue.empty():
        (distance, (row, col)) = queue.get()
        
        visited[row,col] = 1
            
        for neighbor in neighbors:
            neighbor_row = row + neighbor[0]
            neighbor_col = col + neighbor[1]
            if neighbor_row < 0 or neighbor_col < 0 or neighbor_row >= cave.shape[0] or neighbor_col >= cave.shape[1]:
                continue
                
            if visited[neighbor_row,neighbor_col] > 0:
                continue
                
            old_cost = cost_matrix[neighbor_row, neighbor_col]
            new_cost = cost_matrix[row, col] + cave[neighbor_row, neighbor_col]
            if new_cost < old_cost:
                queue.put((new_cost,(neighbor_row, neighbor_col)))
                cost_matrix[neighbor_row, neighbor_col] = new_cost
                
    return cost_matrix

def tile_cave(cave, times = 5):

    def make_tile(cave, times, axis):
        tiles = []
        for i in range(times):
            tile = cave + i
            tile[tile > 9] = tile[tile > 9] - 10 + 1
            tiles.append(tile)
        return np.concatenate(tiles, axis=axis)
    
    tile = make_tile(cave, times, axis=1)
    large_cave = make_tile(tile, times, axis=0)
    return large_cave


cost_matrix = find_path_dijkstra(cave)
print('Result part 1: ', cost_matrix[-1,-1])

large_cave = tile_cave(cave, times = 5)
cost_matrix = find_path_dijkstra(large_cave)
print('Result part 2: ', cost_matrix[-1,-1])