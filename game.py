import pygame,sys,random,ships,os
from pygame.locals import *

pygame.init()
pygame.display.set_caption('bobh4')
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED = (255,0,0)
YELLOW= (255,255,0,0)
PURPLE = (69,0,68)
BOARDWIDTH=15
BOARDHEIGHT=11
BOXSIZE=66
FPSCLOCK=pygame.time.Clock()
def main():
        global DISPLAYSURF, _image_library
        _image_library = {} #remembers images that are already loaded so we dont load them from disc every time
        DISPLAYSURF= pygame.display.set_mode((1024,768)) #starts the actual display window
        board = []
        selectedUnitX = None
        selectedUnitY = None
        selectedUnit = None
        activeTeam = 0
        for x in range(BOARDWIDTH): #board is represented as a two dimensional array and gets randomly filled with some ships here
                column = []
                for y in range(BOARDHEIGHT):
                        if random.randint(1,50) <= 3 :
                                column.append(ships.Ship(100,100,20,3,random.randint(0,1),3,x,y))
                                
                        else :
                                column.append(None)
                board.append(column)
       
        while True: #mainloop of the game each loop represents 1 frame
                
                mouseClicked = False
                DISPLAYSURF.fill(BLUE) #paints everything blue

                if selectedUnitX != None :
                        selectedUnit = board[selectedUnitX][selectedUnitY]
                else :
                        selectedUnit = None
                for x in range(BOARDWIDTH):
                        for y in range(BOARDHEIGHT):
                                pygame.draw.rect(DISPLAYSURF,GREEN,(1+x*BOXSIZE,1+y*BOXSIZE,BOXSIZE,BOXSIZE),1) #paints the grid 
                for event in pygame.event.get(): #all player inputs are events and get handled here
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                        elif event.type == MOUSEMOTION:
                                mousex , mousey = event.pos
                        elif event.type == MOUSEBUTTONUP:
                                mousex , mousey  =event.pos
                                mouseClicked = True
                boxx , boxy = getBoxAtPixel (mousex, mousey) 
                if mouseClicked == True and selectedUnitX != None and posFree(board,boxx,boxy) and distance(boxx,boxy,selectedUnitX,selectedUnitY) <= selectedUnit.moveSpeed: #these are the checks for whatever the player actually did
                        board[boxx][boxy] = board[selectedUnitX][selectedUnitY]
                        board[selectedUnitX][selectedUnitY]=None
                        board[boxx][boxy].remainingMoves -=1

                        if board[boxx][boxy].team == 0 :
                                board[boxx][boxy].currentlyInAnimation = True
                                board[boxx][boxy].animationX , board[boxx][boxy].animationY = leftTopCoordsOfBox(selectedUnitX,selectedUnitY)
                                soundObj = pygame.mixer.Sound("SoundsCrate-SciFi-PowerUp1.wav")
                                soundObj.play()
                                
                        if board[boxx][boxy].remainingMoves == 0 :
                                board[boxx][boxy].selected = False
                                selectedUnitX=None
                                selectedUnitY=None
                        else :
                                selectedUnitX=boxx
                                selectedUnitY=boxy
                elif mouseClicked == True and selectedUnitX == None and posFree(board,boxx,boxy) == False and board[boxx][boxy].team == activeTeam and board[boxx][boxy].remainingMoves !=0 :
                        board[boxx][boxy].selected = True
                        selectedUnitX=boxx
                        selectedUnitY=boxy
                elif mouseClicked == True and selectedUnit != None and posFree(board,boxx,boxy) == False and board[boxx][boxy].team != activeTeam and distance(boxx,boxy,selectedUnitX,selectedUnitY)<= selectedUnit.atkrange :
                        attack(board,selectedUnitX,selectedUnitY,boxx,boxy)
                        board[selectedUnitX][selectedUnitY].remainingMoves -=1
                        if board[selectedUnitX][selectedUnitY].remainingMoves == 0 :
                                board[selectedUnitX][selectedUnitY].selected = False
                                selectedUnitX=None
                                selectedUnitY=None
                elif mouseClicked == True and selectedUnit != None and board[boxx][boxy] == selectedUnit:
                        selectedUnitX = None
                        selectedUnitY = None
                        board[boxx][boxy].selected = False
                       
                if boxx != None and boxy != None: #highlights the box the mouse is currently hovering over
                        pygame.draw.rect(DISPLAYSURF,WHITE,(1+boxx*BOXSIZE,1+boxy*BOXSIZE,BOXSIZE,BOXSIZE),2)
                if teamFinished(board,activeTeam):
                        f =lambda x : (x+1) % 2 #just because this obviously needs some lambda
                        activeTeam = f(activeTeam)
                        setToMaxMoves(board,activeTeam)
                drawBoard(board)#draws the ships
                pygame.display.update()#all drawings before were memory only update actually prints it on the screen
                FPSCLOCK.tick(30)#fps setting


def attack(board,attackerX,attackerY,defenderX,defenderY):
        defender = board[defenderX][defenderY]
        attacker = board[attackerX][attackerY]
        if defender.shields > 0 :
                defender.shields -= attacker.damage
        else :
                defender.hp -= attacker.damage
        if defender.hp<=0 :
                board[defenderX][defenderY] = None

def distance(x1,y1,x2,y2) :
        return max([abs(x1-x2),abs(y1-y2)])
        

def setToMaxMoves(board,team):
         shipList = [s for x in board for s in x if s != None and s.team == team]
         for ship in shipList :
                 ship.remainingMoves =2
        
def teamFinished(board,team):
        shipList = [s for x in board for s in x if s != None and s.team == team and s.remainingMoves>0]
        return len(shipList) ==0

def posFree(board,boxx,boxy):
        return (board[boxx][boxy]== None)
                                

def drawBoard(board):
        unitSelected = False
        for x in range(BOARDWIDTH):
                for y in range(BOARDHEIGHT):
                        if board[x][y]!=None :
                                if board[x][y].currentlyInAnimation == True :
                                        ship = board[x][y]
                                        left,top = leftTopCoordsOfBox(x,y)
                                        f = lambda x , y: x+6 if x < y  else x-6 if x > y  else x #and even more lambda the horror continues
                                        ship.animationX = f(ship.animationX,left)
                                        ship.animationY = f(ship.animationY,top)
                                        if ship.animationY == top and ship.animationX == left :
                                                ship.currentlyInAnimation = False
                                        img = get_image("valkyre.jpg")
                                        DISPLAYSURF.blit(img,(ship.animationX,ship.animationY))
                                elif board[x][y].team == 0:
                                        half = int(0.5 * BOXSIZE)
                                        left, top = leftTopCoordsOfBox(x,y)
                                        if board[x][y].selected == True :
                                                unitSelected= True
                                                selectedX, selectedY = x,y
                                        img = get_image("valkyre.jpg")
                                        img.set_colorkey((100,0,0))
                                        DISPLAYSURF.blit(img,(left,top))
                                elif board[x][y].team == 1 :
                                        half = int(0.5 * BOXSIZE)
                                        left,top = leftTopCoordsOfBox(x,y)
                                        if board[x][y].selected == False :
                                                pygame.draw.circle(DISPLAYSURF,RED,(left+half,top+half),half-5)
                                        else:
                                                unitSelected = True
                                                selectedX, selectedY = x,y
                                                pygame.draw.circle(DISPLAYSURF,WHITE,(left + half,top + half),half-5)
        if unitSelected : #draws the purple squares if a unit is selected
                for x in range(selectedX-board[selectedX][selectedY].moveSpeed,selectedX+board[selectedX][selectedY].moveSpeed+1) :
                        for y in range(selectedY-board[selectedX][selectedY].moveSpeed,selectedY+board[selectedX][selectedY].moveSpeed+1) :
                                if x in range(BOARDWIDTH) and y in range(BOARDHEIGHT) :
                                        if board[x][y] == None :
                                                pygame.draw.rect(DISPLAYSURF,PURPLE,(1+x*BOXSIZE,1+y*BOXSIZE,BOXSIZE-1,BOXSIZE-1))
                                        
        
def get_image(path): #looks if the image already is in library if not it loads the image
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
               
def leftTopCoordsOfBox(boxx,boxy):

        left = boxx * BOXSIZE + 1
        top = boxy * BOXSIZE + 1
        return (left,top)

def getBoxAtPixel(x,y):
        for boxx in range(BOARDWIDTH):
                for boxy in range(BOARDHEIGHT):
                        left, top = leftTopCoordsOfBox(boxx,boxy)
                        boxRect = pygame.Rect(left,top,BOXSIZE,BOXSIZE)
                        if boxRect.collidepoint(x,y):
                                return (boxx,boxy)
        return (None, None)

if __name__ == '__main__':
        main()
