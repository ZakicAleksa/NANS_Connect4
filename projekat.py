import numpy as np
import math
from pygame.constants import RESIZABLE
import constant as const
import pygame as pg
import sys


def create_board():
    board = np.zeros((const.ROWS,const.COLUMNS))
    return board
def validation(column,board):
    return board[const.ROWS-1][column]==0

def putPiece(row,column,piece,board):
    board[row][column]=piece

def getNextEmptyRow(column,board):
    for row in range(const.ROWS):
        if board[row][column]==0:
            return row

def flipBoard(board):
    print(np.flip(board,0))#flip board trough x axis

def checkSub(A,piece):
    n,_=A.shape
    same_el=4
    b=False
    for i in range(n):
        j=0
        if piece==A[i][j] and A[i][j+1] ==piece and piece==A[i][j+2] and piece==A[i][j+3]:
            b=True
    for j in range(n):
        i=0
        if piece==A[i][j] and piece==A[i+1][j]  and piece==A[i+2][j] and piece==A[i+3][j]:
            b=True
    sum_r_diag=0
    for i in range(0,n):
        if piece==A[i, n - i - 1]:
            sum_r_diag=sum_r_diag+1
    if sum_r_diag==same_el:
        b=True
    sum_diag=0
    for i in range(0,n):
        if piece==A[i, i]:
            sum_diag=sum_diag+1
    if sum_diag==same_el:
        b=True
    return b


def checkWinn(A,piece):
    n,m = A.shape
    s_new=np.zeros((4,4))
    allSame=False
    for r in range(1,n-2):
        for c in range(1,m-2):
            s_new=A[r-1:r+3,c-1:c+3]
            one_same=checkSub(s_new,piece)
            if  one_same==True:
                allSame=True
    return allSame
       
def drawBoard(board):
    for col in range(const.COLUMNS):
        for row in range(const.ROWS):
            pg.draw.rect(screen,const.GOLD,(col*const.SQUARESIZE,row*const.SQUARESIZE+const.SQUARESIZE,const.SQUARESIZE,const.SQUARESIZE))
            pg.draw.circle(screen,const.DARK_GRAY,(int(col*const.SQUARESIZE+const.SQUARESIZE/2),int(row*const.SQUARESIZE+const.SQUARESIZE+const.SQUARESIZE/2)),const.RADIUS)
    for col in range(const.COLUMNS):
        for row in range(const.ROWS):
            if board[row][col]==1:
                pg.draw.circle(screen,const.RED,(int(col*const.SQUARESIZE+const.SQUARESIZE/2),const.HEIGHT-int(row*const.SQUARESIZE+const.SQUARESIZE/2)),const.RADIUS)
            elif board[row][col]==-1:
                pg.draw.circle(screen,const.SKYBLUE,(int(col*const.SQUARESIZE+const.SQUARESIZE/2),const.HEIGHT-int(row*const.SQUARESIZE+const.SQUARESIZE/2)),const.RADIUS)
    pg.display.update()

board = create_board()
gameOver=np.False_
turn = 1
pg.display.init()
pg.init()
size=(const.WIDTH,const.HEIGHT)
screen = pg.display.set_mode(size)
pg.display.set_caption('Connect 4')
drawBoard(board)
pg.display.update()
myfont = pg.font.SysFont("Segoe UI", 70)
while not gameOver:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEMOTION:
            pg.draw.rect(screen,const.DARK_GRAY,(0,0,const.WIDTH,const.SQUARESIZE))
            posx = event.pos[0]
            if turn ==1:
                pg.draw.circle(screen,const.RED,(posx,int(const.SQUARESIZE/2)),const.RADIUS)
            else:
                pg.draw.circle(screen,const.SKYBLUE,(posx,int(const.SQUARESIZE/2)),const.RADIUS)
        pg.display.update()
        if event.type == pg.MOUSEBUTTONDOWN :
            pg.draw.rect(screen,const.DARK_GRAY,(0,0,const.WIDTH,const.SQUARESIZE))
            # #player 1 turn
            if turn ==1:
                posx = event.pos[0]
                posy= int(math.floor(posx/const.SQUARESIZE))
                if validation(posy,board):
                    row=getNextEmptyRow(posy,board)
                    putPiece(row,posy,1,board)
                    if checkWinn(board,1):
                        label = myfont.render("Pobednik je igrac 1!", 1, const.RED)
                        screen.blit(label, (50,10))
                        pg.display.update()
                        gameOver=np.True_;
                        

            #plyer 2 turn
            else:
                posx = event.pos[0]
                posy= int(math.floor(posx/const.SQUARESIZE))
                if validation(posy,board):
                    row=getNextEmptyRow(posy,board)
                    putPiece(row,posy,-1,board)
                    if checkWinn(board,-1):
                        label = myfont.render("Pobednik je igrac 2!", 1, const.SKYBLUE)
                        screen.blit(label, (50,10))
                        pg.display.update()
                        gameOver=np.True_;
                        
            flipBoard(board)
            drawBoard(board)
            turn=turn+1
            turn = turn % 2
            if(gameOver):
                pg.time.wait(2000)
        


