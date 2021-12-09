import numpy as np
import sys

# https://adventofcode.com/2021/day/8


file = open('input.txt', 'r')
lines = file.readlines()

segments = []
for line in lines:
    segments.append([x.split(' ') for x in line.rstrip().split(' | ')])


# get all values behind | to count part 1
flat_list = [item for sublist in segments for item in sublist[1]]
print('Result part 1: ', len([segment for segment in flat_list if len(segment) == 2 or len(segment) == 3 or len(segment) == 4 or len(segment) == 7]))




charToPos = {}
charToPos['a'] = 0
charToPos['b'] = 1
charToPos['c'] = 2
charToPos['d'] = 3
charToPos['e'] = 4
charToPos['f'] = 5
charToPos['g'] = 6

# use binary codes for abcdefg
digits_letters = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
digits = {}
for i in range(len(digits_letters)):
    code = [0,0,0,0,0,0,0]
    for char in digits_letters[i]:
        code[charToPos[char]] = 1
    digits[i] = code 

def match_connections(connections, digit_code, segment_code):
    for i, connection_segments in connections.items():
        if digit_code[i] == 0:
            connections[i] = [0 if segment_i == 1 else connection_i for connection_i, segment_i in zip(connection_segments, segment_code)]
        else:
            connections[i] = [1 if connection_i == 1 and segment_i == 1 else 0 for connection_i, segment_i in zip(connection_segments, segment_code)]

def logical_and(left, right):
        and_result = [0, 0, 0, 0, 0, 0, 0]
        return [1 if l == 1 and r == 1 else 0 for (l, r) in zip(left,right)]

def logical_xor(left, right):
    return [1 if (l == 1 and r == 0) or (l == 0 and r == 1) else 0 for (l, r) in zip(left,right)]
    
def logical_xor_3(first, second, third):
    return [0 if (l == 1 and r == 1 and u == 1) or (l == 0 and r == 0 and u == 0) else 1 for (l, r, u) in zip(first, second, third)]



total_sum = 0
for idx in range(len(segments)):
       
    connections = {}
    for i in range(7):
        connections[i] = [1,1,1,1,1,1,1]
        
        
    segments[idx][0] = sorted(segments[idx][0], key=len)

    segment_codes = []
    for segment in segments[idx][0]:
        segment_code = [0,0,0,0,0,0,0]
        
        for char in segment:
            segment_code[charToPos[char]] = 1
        segment_codes.append(segment_code)


    
        
    # first, deduce the simple ones (1,4,7,8)
    for segment_code in segment_codes:
        for digit, digit_code in digits.items():
            if digit_code.count(1) == 2 or digit_code.count(1) == 3 or digit_code.count(1) == 4 or digit_code.count(1) == 7:
                if digit_code.count(1) == segment_code.count(1):
                    # same amount of segments
                    match_connections(connections, digit_code, segment_code)

    # second, use some basic logic to deduce the other ones, sadly above code does not work for this
    if logical_and(segment_codes[0], segment_codes[6]).count(1) == 1:
        connections[5] = logical_and(segment_codes[0], segment_codes[6])
    elif logical_and(segment_codes[0], segment_codes[7]).count(1) == 1:
        connections[5] = logical_and(segment_codes[0], segment_codes[7])
    else:
        connections[5] = logical_and(segment_codes[0], segment_codes[8])

    connections[2] = logical_xor(connections[2], connections[5])
    connections[3] = logical_and(segment_codes[2], logical_and(logical_and(segment_codes[3], segment_codes[4]), segment_codes[5]))
    connections[4] = logical_xor(connections[3], logical_xor(connections[2], logical_xor_3(segment_codes[6], segment_codes[7], segment_codes[8])))
    connections[6] = logical_xor(connections[6],connections[4])
    connections[1] = logical_xor(connections[1],connections[3])

    # create a map for converting connections to appropriate digit
    segment_map = {}
    for i, connection_segments in connections.items():
        segment_map[connection_segments.index(1)] = i

    
    # find correct digit and fill in result
    def match_codes(l, r):
        match = True
        for i in range(len(l)):
            if l[i] is not r[i]:
                return False
        return True
        
        
    result = 0
    power = 1
    for c in reversed(range(len(segments[idx][1]))):
        segment = segments[idx][1][c]
        code = [0,0,0,0,0,0,0]
        for char in segment:
            code[segment_map[charToPos[char]]] = 1
        
        resulting_digit = -1
        for digit, digit_code in digits.items():
            if match_codes(digit_code, code):
                resulting_digit = digit
                break
        result += resulting_digit * power
        power *= 10
    total_sum += result
    
print('Result part 2: ', total_sum)
            
