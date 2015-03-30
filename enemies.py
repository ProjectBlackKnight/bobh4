rocketTooth = enemies.Enemy("RocketTooth", 240, 60, 1, 4, 4, 1, 1)
theSign = enemies.Enemy("TheSign", 400, 110, 2, 7, 5, 1, 3)
skull = enemies.Enemy("Skull", 700, 150, 3, 9, 3, 1, 5)
pentagram = enemies.Enemy("Pentagram", 666, 0, 4, 10, 3, 1, 0)


class Enemy:
    def __init__(self, name, hp, damage, value, prob, movespeed, team, atkrange, x, y):
        self.hp = hp
        self.damage = damage
        self.moveSpeed = movespeed
        self.team = team
        self.atkrange = atkrange
        self.remainingMoves = 2
        self.selected = False
        self.currentlyInAnimation = False
        self.animationX = 0
        self.animationY = 0
        self.x = x
        self.y = y
        self.image = "path"
        self.name = name
        self.value = value
        self.prob = prob


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



