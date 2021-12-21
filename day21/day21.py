# https://adventofcode.com/2021/day/21
import itertools
import copy
import numpy as np

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


def part1(start_pos_player1, start_pos_player2):        
    dice = DeterministicDice(100)
    player1 = Pawn(start_pos_player1, game_board_size=10)
    player2 = Pawn(start_pos_player2, game_board_size=10)
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

    
cache = {}    
combinations = [p for p in itertools.product([1,2,3], repeat=3)]
def play_nextround(players, current_player):
    wins = np.array([0,0], dtype=np.int64)
    hash = (players[0].get_position(), players[0].score(),players[1].get_position(), players[1].score(),current_player)
    if hash in cache:
        wins = cache[hash]
    else:
        for combination in combinations:
            new_players = copy.deepcopy(players) 
            new_players[current_player].go_forward(combination[0] + combination[1] + combination[2] )
            if new_players[current_player].score() >= 21:
                wins[current_player] += 1
            else:
                wins += play_nextround(new_players, 1-current_player)
        cache[hash] = wins
    return wins


def part2(start_pos_player1, start_pos_player2):
    player1 = Pawn(start_pos_player1, game_board_size=10)
    player2 = Pawn(start_pos_player2, game_board_size=10)
    players = [player1,player2]
    wins = play_nextround(players, 0)
    return np.max(wins)


print('Result part 1: ', part1(start_pos_player1 = 7, start_pos_player2 = 2))
print('Result part 2: ', part2(start_pos_player1 = 7, start_pos_player2 = 2))
