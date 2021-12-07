import numpy as np
import sys

# https://adventofcode.com/2021/day/7


file = open('input.txt', 'r')
crabs  = [(int(x)) for x in file.read().split(',')]

def get_fuel_alignment(rate = 'constant'):
    min_fuel_cost = sys.maxsize
    target_alignment = None
    for alignment in range(max(crabs)+1):
        if rate is 'constant':
            fuel_cost = sum([abs(crab-alignment) for crab in crabs])
        elif rate is 'linear':
            fuel_costs = [abs(crab-alignment) for crab in crabs]
            fuel_cost = sum([int(fuel_cost * (fuel_cost + 1) / 2) for fuel_cost in fuel_costs])
            
        if fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
            target_alignment = alignment
    return min_fuel_cost, target_alignment


print('Result part 1: Fuel: %d, Alignment: %d'%get_fuel_alignment(rate = 'constant'))
print('Result part 2: Fuel: %d, Alignment: %d'%get_fuel_alignment(rate = 'linear'))