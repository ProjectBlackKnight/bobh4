class Enemy:
    def __init__(self,name,hp,damage,value,prob,movespeed,team,atkrange,x,y):
        self.name =name
		self.hp = hp
        self.damage = damage
        self.value = value
        self.prob =prob
        self.moveSpeed = movespeed
        self.team = team
        self.atkrange = atkrange
        self.remainingMoves = 2
        self.selected = False
        self.currentlyInAnimation=False
        self.animationX=0
        self.animationY=0
        self.x=x
        self.y=y
        self.image="path"
        
