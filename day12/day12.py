import numpy as np
import cv2


# https://adventofcode.com/2021/day/12


file = open('input.txt', 'r')
lines = file.readlines()

caves  = {}
for line in lines:
    cave = line.rstrip().split('-')
    
    if cave[0] in caves:
        caves[cave[0]].append(cave[1])
    else:
        caves[cave[0]] = [cave[1]]
        
    if cave[1] in caves:
        caves[cave[1]].append(cave[0])
    else:
        caves[cave[1]] = [cave[0]]
        
        

num_paths = 0
visited = {}

def find_paths_part1(cave, path):
    global paths, num_paths
    visited[cave] = True
    
    if cave == 'end':
        num_paths += 1
        visited.pop(cave, None)
        return
        
    for connection in caves[cave]:
        if (connection.islower() and not connection in visited) or connection.isupper():
            find_paths_part1(connection, path)
            
    
    visited.pop(cave, None)
    
    
find_paths_part1('start', [])
print('Result part 1 ', num_paths)


# part 2

num_paths = 0
visited = {}

for key in caves:
    visited[key] = 0

def find_paths_part2(cave, path, twice):
    global paths, num_paths
    visited[cave] += 1
    # path.append(cave)
    if cave == 'end':
        num_paths += 1
        visited[cave] -= 1
        return
        
        
    for connection in caves[cave]:
        if connection == 'start':
            continue
            
        if twice is True:
            if (connection.islower() and visited[connection] < 1) or connection.isupper():
                find_paths_part2(connection, path, twice)
        else:
            if (connection.islower() and visited[connection] < 1) or connection.isupper():
                find_paths_part2(connection, path, twice)
            elif connection.islower() and visited[connection] < 2:
                find_paths_part2(connection, path, True)
        
        
            
    
    visited[cave] -= 1
    
find_paths_part2('start', [], False)
print('Result part 2 ', num_paths)

