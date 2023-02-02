import numpy as np
import constant as const

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
    np.flip(board,0)#flip board trough x axis

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
       