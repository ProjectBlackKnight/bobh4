import pygame,sys,random
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Hello World')
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
YELLOW= (255,255,0,0)
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
        for x in range(BOARDWIDTH):
                column = []
                for y in range(BOARDHEIGHT):
                        if random.randint(1,20) <= 3 :
                                column.append(1)
                        else :
                                column.append(None)
                board.append(column)
        while True: #this is how you comment
                
                mouseClicked = False
                DISPLAYSURF.fill(BLUE)
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
                if mouseClicked == True and selectedUnitX != None and posFree(board,boxx,boxy):
                        
                        board[boxx][boxy] = 1
                        board[selectedUnitX][selectedUnitY]=None
                        selectedUnitX=None
                        selectedUnitY=None
                elif mouseClicked == True and selectedUnitX == None and posFree(board,boxx,boxy) == False:
                        board[boxx][boxy] = 2
                        selectedUnitX=boxx
                        selectedUnitY=boxy
                       
                if boxx != None and boxy != None:
                        pygame.draw.rect(DISPLAYSURF,WHITE,(1+boxx*BOXSIZE,1+boxy*BOXSIZE,BOXSIZE,BOXSIZE),2)
                drawBoard(board)
                pygame.display.update()
                FPSCLOCK.tick(30)


def posFree(board,boxx,boxy):
        return (board[boxx][boxy]== None)
                                

def drawBoard(board):
        for x in range(BOARDWIDTH):
                for y in range(BOARDHEIGHT):
                        if board[x][y] == 1:
                                half = int(0.5 * BOXSIZE)
                                left, top = leftTopCoordsOfBox(x,y)
                                pygame.draw.circle(DISPLAYSURF,YELLOW,(left + half,top + half),half-5)
                        elif board[x][y] == 2 :
                                half = int(0.5 * BOXSIZE)
                                left,top = leftTopCoordsOfBox(x,y)
                                pygame.draw.circle(DISPLAYSURF,WHITE,(left+half,top+half),half-5)

               
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
