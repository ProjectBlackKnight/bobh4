import pygame,sys,random,ships, os, enemies
from pygame.locals import *

class RocketTooth(Enemy):

    def __init__(self):
        super.__init__(name, hp, damage, movespeed, atkrange, value, prob)
        self.name = "RocketTooth"
        self.hp = 240
        self.damage = 60
        self.aktrange = 1
        self.movespeed = 4
        self.value = 1
        self.prob = 4




