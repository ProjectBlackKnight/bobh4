class Ship:
    def __init__(self,hp,shields,damage,movespeed,team,atkrange):
        self.hp = hp
        self.shields = shields
        self.damage = damage
        self.moveSpeed = movespeed
        self.team = team
        self.atkrange = atkrange
        self.remainingMoves = 2
        self.selected = False
