# https://adventofcode.com/2021/day/19
import numpy as np
from itertools import permutations,combinations
import re 

file = open('input.txt', 'r')


scannners_data = file.read().split('\n\n')
scanners = []
for scanner in scannners_data:
    scanner_data = scanner.split('\n')
    target_area = re.findall(r'(-?\d+),(-?\d+),(-?\d+)', scanner_data[1])[0]
    points = []
    for i in range(1,len(scanner_data)):
        point = re.findall(r'(-?\d+),(-?\d+),(-?\d+)', scanner_data[i])[0]
        points.append(point)
    
    scanners.append(np.asarray(points, dtype=np.float64))





def euler_to_rotMat(yaw, pitch, roll):
    Rz_yaw = np.array([
    [np.cos(yaw), -np.sin(yaw), 0],
    [np.sin(yaw), np.cos(yaw), 0],
    [0, 0, 1]
    ])
    Ry_pitch = np.array([
    [np.cos(pitch), 0, np.sin(pitch)],
    [0, 1, 0],
    [-np.sin(pitch), 0, np.cos(pitch)]
    ])
    Rx_roll = np.array([
    [1, 0, 0],
    [0, np.cos(roll), -np.sin(roll)],
    [0, np.sin(roll), np.cos(roll)]
    ])
    # R = RzRyRx
    rotMat = np.dot(Rz_yaw, np.dot(Ry_pitch, Rx_roll))
    return rotMat

Rmat = euler_to_rotMat(0.0, 1.0, 0.0)

permutations = list(permutations([0, np.pi/2.0, np.pi, 3*np.pi/2]))

possible_rotations = [euler_to_rotMat(permutation[0],permutation[1],permutation[2]) for permutation in permutations]




print(np.matmul(scanners[0],possible_rotations[0]))
print(np.matmul(scanners[0],possible_rotations[1]))

print([i for i in range(len(scanners[0]))])
comb = list(combinations(scanners[0], 3))

def align(reference, target):
    reference_point_combinations = list(combinations([i for i in range(len(reference))], 3))
    target_point_combinations = list(combinations([i for i in range(len(target))], 3))
    
    count = 0
    for rotation in possible_rotations:
        target_rotated = np.transpose(np.matmul(rotation, np.transpose(target)))
        for points_ref in reference_point_combinations:
            center_ref = reference[reference_point_combinations[0],:] + reference[reference_point_combinations[1],:] + reference[reference_point_combinations[2],:] / 3
            for points_target in target_point_combinations:
                center_target = target_rotated[target_point_combinations[0],:] + target_rotated[target_point_combinations[1],:] + target_rotated[target_point_combinations[2],:] / 3
                
                translation = center_target - center_ref
                count += 1

align(scanners[0], scanners[1])