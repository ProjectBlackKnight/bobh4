import pygame,sys,random,ships, os
from pygame.locals import *

class Enemy(Ship):
    def __init__(self, name, hp, damage, movespeed, atkrange, value, prob):
        super.__init__(name, hp, damage, movespeed, atkrange)
        self.team = 1
        self.value = value
        self.prob = prob

def creatRT():
    rtname="RocketTooth"
    rthp=240
    rtdamage=60
    rtvalue=1
    rtprob=4
    rtmovespeed=4
    rtatkrange=1
    rocketTooth = Enemy(rtname, rthp, rtdamage, rtmovespeed, rtatkrange, rtvalue, rtprob
    return rocketTooth






"""
    ROCKETTOOTH = Enemy()
    ROCKETTOOTH.name = "RocketTooth"
    ROCKETTOOTH.hp = 240
    ROCKETTOOTH.damage = 60
    ROCKETTOOTH.value = 1
    ROCKETTOOTH.prob = 4
    ROCKETTOOTH.moveSpeed = 4
    ROCKETTOOTH.team = 1
    ROCKETTOOTH.atkrange = 1

    THESIGN = Enemy()
    THESIGN.name = "TheSign"
    THESIGN.hp = 400
    THESIGN.damage = 110
    THESIGN.value = 2
    THESIGN.prob = 7
    THESIGN.moveSpeed = 5
    THESIGN.team = 1
    THESIGN.atkrange = 3

    SKULL = Enemy()
    SKULL.name = "Skull"
    SKULL.hp = 700
    SKULL.damage = 150
    SKULL.value = 3
    SKULL.prob = 9
    SKULL.moveSpeed = 3
    SKULL.team = 1
    SKULL.atkrange = 5

    PENTAGRAM = Enemy()
    PENTAGRAM.name = "Pentagram"
    PENTAGRAM.hp = 666
    PENTAGRAM.damage = 0
    PENTAGRAM.value = 4
    PENTAGRAM.prob = 10
    PENTAGRAM.moveSpeed = 3
    PENTAGRAM.team = 1
    PENTAGRAM.atkrange = 0


def getRT():
    return ROCKETTOOTH


def getTS():
    return THESIGN


def getSK():
    return SKULL


def getPG():
    return PENTAGRAM
"""


