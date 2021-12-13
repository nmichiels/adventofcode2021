import numpy as np
import cv2


# https://adventofcode.com/2021/day/13


file = open('input.txt', 'r')
data = file.read().split('\n\n')
dots = [dot.split(',') for dot in data[0].split('\n')]
dots = [[int(dot[0]),int(dot[1])] for dot in dots]
instructions = data[1].split('\n')
instructions = [instruction.split(' ')[-1].split('=') for instruction in instructions]
max_x = max(dots, key = lambda t: t[0])[0]
max_y = max(dots, key = lambda t: t[1])[1]
page = np.zeros((max_y+1,max_x+1), dtype=np.int16)
for dot in dots:
    page[dot[1],dot[0]] = 1
    
    
    
def fold_page(page, instruction):
    if instruction[0] == 'y':
        fold_line = int(instruction[1])
        if (page.shape[0] % 2) == 0:
            page = np.append(page, np.zeros((1,page.shape[1])), axis=0)
        page =  page[0:fold_line,:] + np.flipud(page[fold_line+1:,:])
        
    if instruction[0] == 'x':
        fold_line = int(instruction[1])
        page =  page[:,0:fold_line] + np.fliplr(page[:,fold_line+1:])
        
    return page
        

def print_page(page):
    for row in range(page.shape[0]):
        for col in range(page.shape[1]):
            if page[row,col] == 0:
                print('.', end = '')
            else:
                print('#', end = '')
        print('')
        

# first fold
page = fold_page(page, instructions[0])
print('Result part 1: ', np.sum(page>0))

# rest of the folds
for i in range(1, len(instructions)):
    page = fold_page(page, instructions[i])

# Resulting code is drawn in console
print('Result part 2: ')
print_page(page)

