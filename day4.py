import numpy as np

# https://adventofcode.com/2021/day/4


with open("input.txt") as file:
    lines = file.readlines()
    lines = [' '.join(line.rstrip().split()) for line in lines]
    
    
drawn = [int(number) for number in lines[0].strip().split(',')]
boards_data = lines[1:]

boards = []
masks = []
for i in range(0,len(boards_data), 6):
    board = ' '.join(boards_data[i+1:i+6])
    
    board = np.fromstring(board, dtype=np.int16, sep=' ').reshape((5,5))
    boards.append(board)
    
    mask = np.zeros((5, 5), dtype=np.bool_)
    masks.append(mask)
    
    
def draw_number(number):
    for i in range(len(boards)):
        masks[i] = np.logical_or(masks[i], boards[i] == number)
    
def check_bingo():
    bingo = []
    for i in range(len(boards)):
        if (5 in np.sum(masks[i], axis=0)) or (5 in np.sum(masks[i], axis=1)):
            #BINGO
            bingo.append(i)
    if len(bingo) > 0:
        return bingo
    else:
        return None
    
winning_boards = []
for number in drawn:
    draw_number(number)
    board_ids = check_bingo()
    if board_ids is not None:
        # BINGO
        for board_id in board_ids: # multiple bingo's at once
            sum = (np.sum(boards[board_id][np.logical_not(masks[board_id])]))
            winning_boards.append((board_id, number, sum, number*sum))
            
        # remove bingo boards
        for board_id in sorted(board_ids, reverse=True):
            del boards[board_id]
            del masks[board_id]

    
    
print('Result part 1: ', winning_boards[0])
print('Result part 2: ', winning_boards[-1])
