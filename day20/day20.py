# https://adventofcode.com/2021/day/20
import numpy as np

file = open('input.txt', 'r')

enhancement_algorithm = [1 if char == '#' else 0 for char in file.readline().rstrip()]

input_image = [line.rstrip() for line in file.readlines()][1:]
for i in range(len(input_image)):
    input_image[i] = [1 if char == '#' else 0 for char in input_image[i]]
input_image = np.asarray(input_image, dtype=np.int16)

def bits2int(bits):
    out = 0
    for bit in bits:
        out = (out << 1) | bit
    return out
    

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    


neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]

for i in range(50):
    input_image = np.pad(input_image, 2, pad_with, padder=i%2)
    output_image = np.zeros(input_image.shape, dtype=np.int16)
    for row in range(1,input_image.shape[0]-1):
        for col in range(1,input_image.shape[1]-1):
            binary = [input_image[row+neighbor[0], col+neighbor[1]] for neighbor in neighbors]
            output_image[row,col] = enhancement_algorithm[bits2int(binary)]
            
    input_image = output_image[1:-1,1:-1] # remove padding
    
    if i == 1:
        print('Result part 1: ', np.sum(input_image))

print('Result part 2: ', np.sum(input_image))


