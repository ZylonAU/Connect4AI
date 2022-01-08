#!/usr/bin/env python3

import pygame as pg
import numpy as np

pg.init()
font = pg.font.SysFont('arial', 25)
    
# rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

BLOCK_SIZE = 20
WIDTH = 640
HEIGHT = 480

class Game:
    def __init__(self, rows=6, cols=7):  
        self.rows = rows
        self.cols = cols      
        
        # init display
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Connect 4')

    def _get_board(self):
        pass

    def _get_legal_moves(self):
        pass

    def _find_winner(self):
        pass

    def play_move(self, move):
        pass

    def draw_board(self):
        pass

    def reset(self):
        pass

if __name__ == '__main__':
    Game()