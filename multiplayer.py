import numpy as np
import math
from pygame.constants import RESIZABLE
import constant as const
import pygame as pg
import sys
from basicFunctions import *
from minimaxFunc import *
       
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
def init_multiplayer():
    board = create_board()
    gameOver=np.False_
    turn = 1
    pg.display.init()
    pg.init()
    pg.display.set_caption('2 Players Mode')
    drawBoard(board)
    pg.display.update()
    myfont = pg.font.SysFont("Segoe UI", 60)
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
                            label = myfont.render("RED player wins!", 1, const.RED)
                            screen.blit(label, (50,10))
                            pg.display.update()
                            gameOver=np.True_;
                        elif  len(get_valid_cols(board))==0:
                            label = myfont.render("                TIE!", 1, const.GREEN)
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
                            label = myfont.render("BLUE player wins!", 1, const.SKYBLUE)
                            screen.blit(label, (50,10))
                            pg.display.update()
                            gameOver=np.True_;
                        elif  len(get_valid_cols(board))==0:
                            label = myfont.render("                TIE!", 1, const.GREEN)
                            screen.blit(label, (50,10))
                            pg.display.update()
                            gameOver=np.True_;
                            
                flipBoard(board)
                drawBoard(board)
                turn=turn+1
                turn = turn % 2
                if(gameOver):
                    pg.time.wait(2000)
        


