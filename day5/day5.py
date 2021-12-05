import numpy as np
import re

# https://adventofcode.com/2021/day/5


file = open('input.txt', 'r')
vent_lines = [(int(x1),int(y1),int(x2),int(y2)) for x1, y1, x2, y2 in re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', file.read())]

def get_dimension(vent_lines):
    width = max(max(vent_lines, key = lambda t: t[0])[0], max(vent_lines, key = lambda t: t[2])[2]) + 1
    height = max(max(vent_lines, key = lambda t: t[1])[1], max(vent_lines, key = lambda t: t[3])[3]) + 1
    return height, width
     
height, width = get_dimension(vent_lines)


with_diagonal = True  # set True for part 2

seabed = np.zeros((height, width), dtype=np.int16)
for (x1,y1,x2,y2) in vent_lines:
    if (x1 == x2) or (y1 == y2):
        x_range = np.linspace(x1,x2, np.abs(x2-x1)+1, dtype=np.int16)
        y_range = np.linspace(y1,y2, np.abs(y2-y1)+1, dtype=np.int16)
        seabed[y_range, x_range] += 1
    else:
        # diagonal
        if with_diagonal:
            diag_range = np.linspace((x1,y1),(x2,y2),np.abs(x2-x1)+1, dtype=np.int16)
            for i in diag_range:
                seabed[i[1],i[0]] += 1
        
print('Result: ', (seabed > 1).sum())
