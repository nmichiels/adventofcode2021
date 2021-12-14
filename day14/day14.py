import numpy as np
import re
from string import ascii_uppercase

# https://adventofcode.com/2021/day/14


file = open('input.txt', 'r')
template = file.readline().rstrip()
rules = {}
for pair, insertion in re.findall(r'([A-Z]+) -> ([A-Z]+)', file.read()):
    rules[pair] = insertion


def init_occurences():
    occurences = {}
    for c in ascii_uppercase:
        occurences[c] = 0
    return occurences
        
def grow_polymer(polymer, rules, steps=1):
    result = polymer
    for step in range(steps):
        new_polymer = []
        for i in range(len(result)-1):
            new_polymer.append(result[i])
            new_polymer.append(rules[result[i]+result[i+1]])
        new_polymer.append(result[-1])    
        result = new_polymer
    return result
        
     
        
def part1(template, rules):
    polymer = template

    polymer = grow_polymer(polymer, rules, steps=10)

    occurences = [(x,polymer.count(x)) for x in set(polymer)]

    max_occurence = max(occurences, key = lambda i : i[1])
    min_occurence = min(occurences, key = lambda i : i[1])
    
    return max_occurence[1] - min_occurence[1]

def build_cache(rules):
    cache = {}
    for rule in rules:
        print(rule)
        pol = grow_polymer(rule, rules, steps = 20)
        occurences = init_occurences()
        for char in pol:
            occurences[char] += 1
        cache[rule] = (pol, occurences)
    return cache
        
def part2(template, rules):


    #build cache of rules for depth 20
    cache = build_cache(rules)
    
    polymer = grow_polymer(template, rules, steps = 20)
    
    total_occurences = init_occurences()
    for i in range(len(polymer)-1):
        test = cache[polymer[i]+polymer[i+1]][1]
        # todo sum all occurences and take care of the duplicates of the first and last character

    occurences = [(x,polymer.count(x)) for x in set(polymer)]

    max_occurence = max(occurences, key = lambda i : i[1])
    min_occurence = min(occurences, key = lambda i : i[1])
    
    print( max_occurence[1] - min_occurence[1])
    





print('Result part 1: ', part1(template, rules))

print('Result part 2 ', part2(template, rules))





