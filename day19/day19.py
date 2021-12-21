# https://adventofcode.com/2021/day/19
import numpy as np
import itertools
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
    
    scanners.append(np.asarray(points, dtype=np.int))





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

# permutations = list(permutations([0, np.pi/2.0, np.pi, 3*np.pi/2]))
# permutations = [p for p in itertools.product([0, np.pi/2.0, np.pi, 3*np.pi/2], repeat=3)]

# possible_rotations = [euler_to_rotMat(permutation[0],permutation[1],permutation[2]) for permutation in permutations]

# flipx = np.identity(3, dtype=np.int)
# flipx[0,0] = -1
# flipy = np.identity(3, dtype=np.int)
# flipy[1,1] = -1
# flipz = np.identity(3, dtype=np.int)
# flipz[2,2] = -1


yz = np.zeros((3,3), dtype=np.int)
yz[0,0] = 1
yz[1,2] = 1
yz[2,1] = 1
xy = np.zeros((3,3), dtype=np.int)
xy[0,1] = 1
xy[1,0] = 1
xy[2,2] = 1
xz = np.zeros((3,3), dtype=np.int)
xz[0,2] = 1
xz[1,1] = 1
xz[2,0] = 1
possible_flips = [np.identity(3), yz, xy, xz]

possible_rotations = []
for t in itertools.product([1, -1], repeat=3):
    rotation = np.identity(3, dtype=np.int)
    for i in range(3):
        rotation[i,i] = t[i]
   
    for possible_flip in possible_flips:
        possible_rotations.append(np.matmul(rotation,possible_flip))
    
print((possible_rotations))

# possible_rotations = [(np.matmul(possible_rotation,flipx),np.matmul(possible_rotation,flipy),np.matmul(possible_rotation,flipz)) for possible_rotation in possible_rotations]
# possible_rotations = [item for sublist in possible_rotations for item in sublist]

# possible_rotations = [flipy]

def check_alignment(map, target, translate):

    num_alignments = 0

    for point in target:
        point_translated = point - translate
        if (point_translated[0],point_translated[1],point_translated[2]) in map:
            num_alignments += 1
    if num_alignments >= 12:
        return True
    else:
        return False
         
# print(np.matmul(scanners[0],possible_rotations[0]))
# print(np.matmul(scanners[0],possible_rotations[1]))

# print([i for i in range(len(scanners[0]))])

def align(reference, target):
    map = {}
    for point in reference:
        map[(point[0],point[1],point[2])] = 1
        
    for rotation in possible_rotations:
        # print(rotation)

        target_rotated = np.transpose(np.matmul(rotation, np.transpose(target))).astype(dtype=np.int)
      
        # for each point in rotated target, check if it aligns with one of the reference points
        for target_point in target_rotated:
            for reference_point in reference:
                translate = target_point-reference_point
                if check_alignment(map, target_rotated, translate):
                    print('alignment found: ', translate, rotation)
        # return
    

align(scanners[0], scanners[1])