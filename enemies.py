import pygame,sys,random,ships, os
from pygame.locals import *

class Enemy(Ship):
    def __init__(self, name, hp, damage, movespeed, atkrange, value, prob):
        super.__init__(name, hp, damage, movespeed, atkrange)
        self.team = 1
        self.value = value
        self.prob = prob

def createRT():
    name = "RocketTooth"
    hp = 240
    damage = 60
    value = 1
    prob = 4
    movespeed = 4
    atkrange = 1
    rocketTooth = Enemy(name, hp, damage, movespeed, atkrange, value, prob)
    return rocketTooth

def createTS():
    name = "TheSign"
    hp = 400
    damage = 110
    value = 2
    prob = 7
    movespeed = 5
    atkrange = 3
    theSign = Enemy(name, hp, damage, movespeed, atkrange, value, prob)
    return theSign

def createSK():
    name = "Skull"
    hp = 700
    damage = 150
    value = 3
    prob = 9
    movespeed = 3
    atkrange = 5
    skull = Enemy(name, hp, damage, movespeed, atkrange, value, prob)
    return skull

def createPG():
    name = "Pentagramm"
    hp = 666
    damage = 0
    value = 4
    prob = 10
    movespeed = 3
    atkrange = 0
    pentagramm = Enemy(name, hp, damage, movespeed, atkrange, value, prob)
    return pentagramm








