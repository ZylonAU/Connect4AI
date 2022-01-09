#!/usr/bin/env python3

import pygame as pg
import numpy as np
from time import sleep

pg.init()
font = pg.font.SysFont('arial', 25)
    
# rgb colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (200,0,0)
BLUE = (0, 100, 255)
PLAYER_COLOURS = [BLACK, BLUE, RED]

class Game:
    def __init__(self, block_size=90, rows=6, cols=7):  
        self.block_size = block_size
        self.rows = rows
        self.cols = cols

        self.players = [1, 2]
        self.start_player = self.players[0]
        self.width = self.block_size * cols
        self.height = self.block_size * rows

        # init display
        self.display = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption('Connect 4')

        self.reset()

    def _get_legal_moves(self):
        pass

    def _setup_board(self):
        ''' Create empty board '''
        return np.zeros((self.rows, self.cols), dtype=int)

    def _find_winner(self):
        pass

    def _is_occupied(self, row, col):
        return bool(self.board[row, col])

    def _play_move(self, move) -> bool:
        ''' 
        Place piece in column. 
        
        :return: True if piece was placed.
        '''
        if move < 0 or move > self.rows:
            return False

        for row in range(self.rows):
            if not self._is_occupied(row, move):
                self.board[row, move] = self.turn
                return True
        return False

    def _get_move(self):
        valid_events = [
            pg.QUIT,
            pg.MOUSEBUTTONDOWN
        ]
        pg.event.set_allowed(valid_events)
        return pg.event.wait()

    def play_step(self):
        self.draw_board()

        # Get move
        valid_move = False
        while not valid_move:
            event = self._get_move()
            match event.type:
                case pg.QUIT:
                    pg.quit()
                    quit()
                case pg.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col = x // self.block_size
                    valid_move = self._play_move(col)

        # Finish turn
        self.turn = self._get_next_player(self.turn)
        self.play_step()


    def draw_board(self):
        self.display.fill(WHITE)
        for row in range(self.rows):
            for col in range(self.cols):
                # Background
                colour = WHITE if (row + col) % 2 else BLACK
                shape = pg.Rect(col * self.block_size, row * self.block_size, self.block_size, self.block_size)

                # Piece
                player = self.board[self.rows - row - 1, col]
                colour = colour if player == 0 else PLAYER_COLOURS[player]

                pg.draw.rect(self.display, colour, shape)
        pg.display.flip()

    def _get_next_player(self, current_player):
        return self.players[(self.players.index(current_player) + 1) % len(self.players)]

    def reset(self):
        self.board = self._setup_board()
        self.turn = self.start_player
        self.start_player = self._get_next_player(self.start_player)
        
        self.play_step()

if __name__ == '__main__':
    Game()
