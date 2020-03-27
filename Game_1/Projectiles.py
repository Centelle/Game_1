import pygame
from Game_1 import Player
from Game_1.Colours import *

class Bullet:
    def __init__(self, x, y, shotBy: Player, win):
        self.x = x
        self.y = y
        self.wid = 20
        self.height = 8
        self.dir = 1 if shotBy.facingRight else -1
        self.vel = 3
        self.win = win
        self.colour = RED

    def draw(self):
        pygame.draw.rect(self.win, self.colour, (self.x, self.y, self.wid, self.height))
        pygame.display.update()

    def move(self):
        self.x += self.vel * self.dir
        self.draw()
