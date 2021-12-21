# https://adventofcode.com/2021/day/21
from itertools import permutations

class DeterministicDice(object):
    def __init__(self, sides = 100):
        self._num_sides = sides
        self._current_side = 0
        self._total_rolls = 0
        
    def roll(self):
        self._current_side += 1
        if self._current_side == 101:
            self._current_side = 1
        self._total_rolls += 1
        return self._current_side
        
    def total_rolls(self):
        return self._total_rolls
        

class Pawn(object):
    def __init__(self, start_position, game_board_size = 10):
        self._position = start_position-1 # Pawn object uses index starting at 0
        self._game_board_size = game_board_size
        self._score = 0
        
    def go_forward(self, steps = 1):
        self._position += steps
        self._position = self._position % self._game_board_size
        self._score += self._position + 1
        
        
    def get_position(self):
        return self._position + 1  # positions start at index 1
        
    
    def score(self):
        return self._score


def part1():        
    dice = DeterministicDice(100)

    player1 = Pawn(7, game_board_size=10)
    player2 = Pawn(2, game_board_size=10)

    players = [player1,player2]
    current_player = 0
    while True:
        player = players[current_player]
        
        
        player.go_forward(dice.roll()+dice.roll()+dice.roll())
        
            
        current_player += 1
        current_player = current_player % 2
        
        if player.score() >= 1000:
            break

    losing_player = players[current_player]
    return losing_player.score() * dice.total_rolls()
    
    
def part2():
    player1 = Pawn(4, game_board_size=10)
    player2 = Pawn(8, game_board_size=10)
    
    combinations = [3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 1]
    
    universes = [(player1,player2, 0)] # last element is current_player: 0 for player 1, 1 for player 2
    
    
    while True:
        (player1, player2, current_player) = universes.pop(0)
        
        for combination in combinations:
            pass
        
        
        if len(universes) == 0:
            break
    
    
    
print('Result part 1: ', part1())

print('Result part 2: ', part2())
