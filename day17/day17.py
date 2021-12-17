# https://adventofcode.com/2021/day/17
import re

file = open('input.txt', 'r')
target_area = re.findall(r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', file.read())[0]
target_x_min = int(target_area[0])
target_x_max = int(target_area[1])
target_y_min = int(target_area[2])
target_y_max = int(target_area[3])

def overshoot(x, y):
    if x > target_x_max or y < target_y_min:
        return True
    return False
    
    
def in_target_area(x, y):
    if x >= target_x_min and x <= target_x_max and y >= target_y_min and y <= target_y_max:
        return True
    else:
        return False
    
    

def check_trajectory(vx, vy, drag = 1, gravity = 1):
    x = 0
    y = 0
    max_y = -9999999
    
    while True:
        x += vx
        y += vy
        max_y = max(y,max_y)
        if vx > 0:
            vx -= 1 
        elif vx < 0:
            vx += 1
        vy -= gravity
        # print(x,y)
        if in_target_area(x, y):
            return True, max_y
            
        if overshoot(x, y):
            return False, max_y
        
    
best_y = -9999999
best_velocity = None
valid_velocities = []
for vx in range(1,500):
    for vy in range(-100,100):
        valid, max_y = check_trajectory(vx, vy)
        if valid:
            valid_velocities.append((vx,vy))
        if valid and max_y > best_y:
            best_y = max_y
            best_velocity = (vx,vy)
            
print('Result part 1: ', best_y)
print('Result part 2: ', len(valid_velocities))