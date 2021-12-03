import numpy as np

# https://adventofcode.com/2021/day/3


# part 1
def split(word):
    return [int(char) for char in word]
    
with open("input.txt") as file:
    lines = file.readlines()
    lines = [split(line.rstrip()) for line in lines]
    lines = np.asarray(lines)

gamma_bin = []
epsilon_bin = []
for c in range(lines.shape[1]):
    (unique, counts) = np.unique(lines[:,c], return_counts=True)
    i = unique[np.argmax(counts), ] # get unique value with max amount of 
    gamma_bin.append(i)
    epsilon_bin.append(1-i)


# converting binary list to integer 
gamma = int("".join(str(x) for x in gamma_bin), 2)
epsilon = int("".join(str(x) for x in epsilon_bin), 2)
print('Result part 1: ', gamma*epsilon)


# part 2
oxygen_candidates = np.copy(lines)
c = 0
while  oxygen_candidates.shape[0] > 1:
    new_oxygen_candidates = np.empty((0,oxygen_candidates.shape[1]), int)
    (unique, counts) = np.unique(oxygen_candidates[:,c], return_counts=True)
    if (counts[0] == counts[1]): #same count
        i = 1
    else:
        i = unique[np.argmax(counts), ] # get unique value with max amount of 
    for r in range(oxygen_candidates.shape[0]):
        if oxygen_candidates[r,c] == i:
            new_oxygen_candidates = np.append(new_oxygen_candidates, np.expand_dims(oxygen_candidates[r,:], axis=0), axis=0)
    oxygen_candidates = np.copy(new_oxygen_candidates)
    c += 1

oxygen_generator_rating = int("".join(str(x) for x in oxygen_candidates[0].tolist()), 2)



co2scrubbing_candidates = np.copy(lines)
c = 0
while  co2scrubbing_candidates.shape[0] > 1:
    new_co2scrubbing_candidates = np.empty((0,co2scrubbing_candidates.shape[1]), int)
    (unique, counts) = np.unique(co2scrubbing_candidates[:,c], return_counts=True)
    if (counts[0] == counts[1]): #same count
        i = 1
    else:
        i = unique[np.argmax(counts), ] # get unique value with max amount of 
    i = 1-i
    for r in range(co2scrubbing_candidates.shape[0]):
        if co2scrubbing_candidates[r,c] == i:
            new_co2scrubbing_candidates = np.append(new_co2scrubbing_candidates, np.expand_dims(co2scrubbing_candidates[r,:], axis=0), axis=0)
    co2scrubbing_candidates = np.copy(new_co2scrubbing_candidates)
    c += 1
CO2_scrubber_rating = int("".join(str(x) for x in co2scrubbing_candidates[0].tolist()), 2)



print('Result part 2: ', oxygen_generator_rating*CO2_scrubber_rating)