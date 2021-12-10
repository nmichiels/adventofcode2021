import numpy as np
import cv2


# https://adventofcode.com/2021/day/10



file = open('input.txt', 'r')
lines = file.readlines()
lines = [line.rstrip() for line in lines]

syntaxerror_scores = {}
syntaxerror_scores[')'] = 3
syntaxerror_scores[']'] = 57
syntaxerror_scores['}'] = 1197
syntaxerror_scores['>'] = 25137


syntaxerror_score = 0
autocomplete_scores = []
for line in lines:
    stack = []
    corrupt = False
    for char in line:
        if char == '(' or char == '<' or char == '[' or char == '{':
            stack.append(char)
        else:
            prev_char = stack.pop()
            if (char == ')' and prev_char == '(') or (char == '>' and prev_char == '<') or (char == ']' and prev_char == '[') or (char == '}' and prev_char == '{'):
                pass # correct chunk
            else:
                # syntax error
                syntaxerror_score += syntaxerror_scores[char]
                corrupt = True
                break
    
    # part 2: incomplete lines
    if not corrupt and len(stack) > 0:
        autocomplete_score = 0
        for i in range(len(stack)):
            prev_char = stack.pop()
            
            autocomplete_score *= 5
            if prev_char == '(':
                # autocomplete with 
                autocomplete_score += 1
            if prev_char == '[':
                # autocomplete with 
                autocomplete_score += 2
            if prev_char == '{':
                # autocomplete with 
                autocomplete_score += 3
            if prev_char == '<':
                # autocomplete with 
                autocomplete_score += 4
        autocomplete_scores.append(autocomplete_score)
        
autocomplete_scores.sort()

                
print('Result part 1: ', syntaxerror_score)
print('Result part 2: ', autocomplete_scores[int((len(autocomplete_scores)-1) / 2)])

                