import pygame as pg
import numpy as np
from Pieces import  *
from Board import *

WIDTH=480
HEIGHT=480
GAME_NAME='Chess'
FPS=60

class Game():
    def __init__(self):
        self.init_pygame()
        self.running=True
        self.paused=False
        self.whiteTurn=True
        self.bottomWhite=True
        self.board=Board()

    def init_pygame(self):
        pg.init()
        self.clock=pg.time.Clock()
        self.win=pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(GAME_NAME)

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running=False

    def draw(self):
        self.drawGrid()
        pg.display.update()

    def drawGrid(self):
        i=True
        for x in range(8):
            for y in range(8):
                if i:
                    pg.draw.rect(self.win,(232,235,239),(x*60,y*60,60,60))
                    i=False
                else:
                    pg.draw.rect(self.win,(125,135,150),(x*60,y*60,60,60))
                    i=True
            i=False if i else True


test=Game()
test.run()
test.board.board[1,0]=1
print(test.board)
print(not False and not True)
