import csv
from random import random
import numpy as np
import math
import random
import constant as const
import pygame as pg
import sys
from basicFunctions import *
from serialization import write
from minimaxFunc import *

COLUMN_NUM = 7
ROW_NUM = 6


       
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



    
size=(const.WIDTH,const.HEIGHT)
screen = pg.display.set_mode(size)
def init_minimax():
    board = create_board()
    gameOver=np.False_
    turn = random.randint(0,1)
    pg.display.init()
    pg.init()
    pg.display.set_caption('Single player vs MiniMax')
    drawBoard(board)
    pg.display.update()
    myfont = pg.font.SysFont("Segoe UI", 60)
    turnArray=[]
    while not gameOver:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEMOTION:
                pg.draw.rect(screen,const.DARK_GRAY,(0,0,const.WIDTH,const.SQUARESIZE))
                posx = event.pos[0]
                if turn ==1:
                    pg.draw.circle(screen,const.RED,(posx,int(const.SQUARESIZE/2)),const.RADIUS)
            pg.display.update()
            if event.type == pg.MOUSEBUTTONDOWN :
                pg.draw.rect(screen,const.DARK_GRAY,(0,0,const.WIDTH,const.SQUARESIZE))
                # #player 1 turn
                if turn == 1:
                    posx = event.pos[0]
                    posy= int(math.floor(posx/const.SQUARESIZE))
                    if validation(posy,board):
                        row=getNextEmptyRow(posy,board)
                        putPiece(row,posy,1,board)
                        if checkWinn(board,1):
                            label = myfont.render("RED player wins!", 1, const.RED)
                            screen.blit(label, (50,10))
                            pg.display.update()
                            gameOver=np.True_;
                        turn = 0
                        flipBoard(board)
                        drawBoard(board)
                        pg.time.wait(500)

                #plyer 2 turn
        if turn ==0 and not gameOver:
            _,col = minimax(4,-math.inf,math.inf,True,board)
            ##col = pick_best_move(board,-1)
            cntTurn=0;
            cntColumn=0;
            turnArray.append(col)
            for  i in range(len(turnArray)):
                cntTurn=i
                cntColumn = turnArray[i]
            write(cntTurn,cntColumn)
            if validation(col,board):
                row=getNextEmptyRow(col,board)
                putPiece(row,col,-1,board)
                if checkWinn(board,-1):
                    label = myfont.render("BLUE player wins!", 1, const.SKYBLUE)
                    screen.blit(label, (50,10))
                    pg.display.update()
                    gameOver=np.True_;
                    
                flipBoard(board)
                drawBoard(board)
                turn=1
        if(gameOver):
            pg.time.wait(2000)
        


