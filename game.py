import pygame,sys,random,ships
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
#fontObj = pygame.font.Font('freesansbold.ttf', 32)
#textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
#textRectObj = textSurfaceObj.get_rect()
#textRectObj.center = (200, 150)
def main():
        global DISPLAYSURF
        DISPLAYSURF= pygame.display.set_mode((1024,768))
        board = []
        selectedUnitX = None
        selectedUnitY = None
        selectedUnit = None
        activeTeam = 0
        for x in range(BOARDWIDTH):
                column = []
                for y in range(BOARDHEIGHT):
                        if random.randint(1,50) <= 3 :
                                column.append(ships.Ship(100,100,20,3,random.randint(0,1),3))
                                
                        else :
                                column.append(None)
                board.append(column)
        while True: #this is how you comment
                
                mouseClicked = False
                DISPLAYSURF.fill(BLUE)
                if selectedUnitX != None :
                        selectedUnit = board[selectedUnitX][selectedUnitY]
                else :
                        selectedUnit = None
                for x in range(BOARDWIDTH):
                        for y in range(BOARDHEIGHT):
                                pygame.draw.rect(DISPLAYSURF,GREEN,(1+x*BOXSIZE,1+y*BOXSIZE,BOXSIZE,BOXSIZE),1)
        #DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                        elif event.type == MOUSEMOTION:
                                mousex , mousey = event.pos
                        elif event.type == MOUSEBUTTONUP:
                                mousex , mousey  =event.pos
                                mouseClicked = True
                boxx , boxy = getBoxAtPixel (mousex, mousey)
                if mouseClicked == True and selectedUnitX != None and posFree(board,boxx,boxy) and distance(boxx,boxy,selectedUnitX,selectedUnitY) <= selectedUnit.moveSpeed:
                        
                        board[boxx][boxy] = board[selectedUnitX][selectedUnitY]
                        board[selectedUnitX][selectedUnitY]=None
                        board[boxx][boxy].remainingMoves -=1
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
                       
                if boxx != None and boxy != None:
                        pygame.draw.rect(DISPLAYSURF,WHITE,(1+boxx*BOXSIZE,1+boxy*BOXSIZE,BOXSIZE,BOXSIZE),2)
                if teamFinished(board,activeTeam):
                        activeTeam = (activeTeam +1) % 2
                        setToMaxMoves(board,activeTeam)
                drawBoard(board)
                pygame.display.update()
                FPSCLOCK.tick(30)


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
        for x in range (BOARDWIDTH):
                for y in range(BOARDHEIGHT):
                        if board[x][y]!=None:
                                if board[x][y].team==team:
                                        board[x][y].remainingMoves = 2
def teamFinished(board,team):
        for x in range (BOARDWIDTH):
                for y in range(BOARDHEIGHT):
                        if board[x][y] != None:
                             if board[x][y].team == team and board[x][y].remainingMoves > 0:
                                     return False
        return True

def posFree(board,boxx,boxy):
        return (board[boxx][boxy]== None)
                                

def drawBoard(board):
        unitSelected = False
        for x in range(BOARDWIDTH):
                for y in range(BOARDHEIGHT):
                        if board[x][y]!=None :    
                                if board[x][y].team == 0:
                                        half = int(0.5 * BOXSIZE)
                                        left, top = leftTopCoordsOfBox(x,y)
                                        if board[x][y].selected == False :
                                                pygame.draw.circle(DISPLAYSURF,YELLOW,(left + half,top + half),half-5)
                                        else:
                                                unitSelected= True
                                                selectedX, selectedY = x,y
                                                pygame.draw.circle(DISPLAYSURF,WHITE,(left + half,top + half),half-5)
                                elif board[x][y].team == 1 :
                                        half = int(0.5 * BOXSIZE)
                                        left,top = leftTopCoordsOfBox(x,y)
                                        if board[x][y].selected == False :
                                                pygame.draw.circle(DISPLAYSURF,RED,(left+half,top+half),half-5)
                                        else:
                                                unitSelected = True
                                                selectedX, selectedY = x,y
                                                pygame.draw.circle(DISPLAYSURF,WHITE,(left + half,top + half),half-5)
        if unitSelected :
                for x in range(selectedX-board[selectedX][selectedY].moveSpeed,selectedX+board[selectedX][selectedY].moveSpeed+1) :
                        for y in range(selectedY-board[selectedX][selectedY].moveSpeed,selectedY+board[selectedX][selectedY].moveSpeed+1) :
                                if x in range(BOARDWIDTH) and y in range(BOARDHEIGHT) :
                                        if board[x][y] == None :
                                                pygame.draw.rect(DISPLAYSURF,PURPLE,(1+x*BOXSIZE,1+y*BOXSIZE,BOXSIZE-1,BOXSIZE-1))
                                        
        

               
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
