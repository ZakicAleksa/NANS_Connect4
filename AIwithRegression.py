import csv
from random import random
from matplotlib import pyplot as plt
import numpy as np
import math
import random
from sympy import true
import constant as const
import pygame as pg
import sys
from regression import *
import serialization 
import pandas as pd
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
def init_regression(mode):
    board = create_board()
    gameOver=np.False_
    turn = random.randint(0,1)
    pg.display.init()
    pg.init()
    pg.display.set_caption('Single player vs Regression models')
    drawBoard(board)
    pg.display.update()
    myfont = pg.font.SysFont("Segoe UI", 60)
    cnt=0
    cnt_l=0
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
            x,y=serialization.read()
            data = pd.DataFrame(np.column_stack([x,y]),columns=['x','y'])
            for i in range(2,16):
                name = 'x_%d'%i
                data[name]=data['x']**i
            #print(data)
            predictors = ['x']
            predictors.extend(['x_%d'%i for i in range(2,16)])
            #When alpha=0 we have linear regression
            #alpha_ridge = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2,0, 1, 5, 10, 20]
            if mode==2 :
                alpha_ridge = [1e-4]
                col_ = ['rss','intercept'] + ['coef_x_%d'%i for i in range(1,16)]
                ind = ['alpha_%.2g'%alpha_ridge[0]]
                coef_matrix_ridge = pd.DataFrame(index=ind, columns=col_)
                coef_matrix_ridge.iloc[0,],pred = ridge_regression(data, predictors, alpha_ridge[0])
                #print(pred)
                col = int(round(abs(pred[cnt])))
                while not validation(col,board):
                    col = random.choice([0,1,2,3,4,5,6])
                cnt=cnt+1
            elif mode==1:
                alpha_lasso=[1e-10]
                col_ = ['rss','intercept'] + ['coef_x_%d'%i for i in range(1,16)]
                ind = ['alpha_%.2g'%alpha_lasso[0]]
                coef_matrix_ridge = pd.DataFrame(index=ind, columns=col_)
                coef_matrix_ridge.iloc[0,],pred = lasso_regression(data, predictors, alpha_lasso[0])
                column = int(round(pred[cnt_l]))
                col = pick_best_move(board,-1,column)
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
     
    
