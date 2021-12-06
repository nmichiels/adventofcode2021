import numpy as np
import re

# https://adventofcode.com/2021/day/6


file = open('input.txt', 'r')
lanternfish_input  = [(int(x)) for x in file.read().split(',')]

def simulate_exponential_growth_lanternfish(lanternfish, days):
    for day in range(days):
        for i in range(len(lanternfish)):
            lanternfish[i] -= 1
            if lanternfish[i] < 0:
                lanternfish[i] = 6
                lanternfish.append(8)
    return lanternfish

# part 1
lanternfish_part1 = simulate_exponential_growth_lanternfish(lanternfish_input.copy(), 80)
print('Result part 1: ', len(lanternfish_part1))


# part 2: first count exponential growth of lanternfish to day 128 for each unique starting state, then combine and reconstruct for day 256
fish_128_days = {}
for unique_i in range(0,9): # a total of 9 starting states possible
    fish = simulate_exponential_growth_lanternfish([unique_i], 128)
    fish_128_days[unique_i] = fish
  
# reconstruct day 256 using lanternfish of 128
lanternfish_256_days = {}
for key, value in fish_128_days.items():
    sum_fish = 0
    for fish in value:
        sum_fish += len(fish_128_days[fish])
    lanternfish_256_days[key] = sum_fish
    
# total laternfish is the sum of all the initial laternfishes
total_lanternfish = 0
for fish in lanternfish_input:
    total_lanternfish += lanternfish_256_days[fish]
print('Result part 2: ', total_lanternfish)