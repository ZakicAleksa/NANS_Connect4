from basicFunctions import *
import numpy as np
import math
import random
COLUMN_NUM = 7
ROW_NUM = 6

def evaluate(part,piece):
    score = 0
    enemy_peace = 1
    if piece == 1:
        enemy_peace=-1
    
    if part.count(piece) == 4:
        score += 100
    elif part.count(piece) == 3 and part.count(0) == 1:
        score += 5
    elif part.count(piece) == 2 and part.count(0) == 2:
        score += 2
    if part.count(enemy_peace) == 3 and part.count(0)==1:
        score -= 20
    return score

def score_move(board,piece):
    score = 0

    center_array = [int(i) for i in list(board[:, COLUMN_NUM//2])]
    center_count = center_array.count(piece)
    score += center_count * 3
    ## VERTICAL
    for i in range(COLUMN_NUM):
        col = [int(k) for k in list(board[:,i])]
        for j in range(ROW_NUM-3):
            part = col[j:j+4]
            score += evaluate(part,piece)

     ## HORIZONTAL
    for i in range(ROW_NUM):
        row = [int(k) for k in list(board[i,:])]
        for j in range(COLUMN_NUM-3):
            part = row[j:j+4]
            score += evaluate(part,piece)

            

    for r in range(ROW_NUM-3):
            for c in range(COLUMN_NUM-3):
                part = [board[r+3-i][c+i] for i in range(4)]   
                score += evaluate(part, piece)

    for r in range(ROW_NUM-3):
        for c in range(COLUMN_NUM-3):
            part = [board[r+3-i][c+i] for i in range(4)]
            score += evaluate(part, piece)

    return score

def get_valid_cols(board):
    valid_cols = []
    for col in range(COLUMN_NUM):
        if(validation(col,board)):
            valid_cols.append(col)
    return valid_cols

def is_game_end(board):
    return checkWinn(board, 1) or checkWinn(board, -1) or len(get_valid_cols(board)) == 0

def minimax(depth,alpha,beta,maximizingPlayer,board):
    valid_moves = get_valid_cols(board)
    is_end = is_game_end(board)

    if depth == 0 or is_end:
        if is_end:
            if checkWinn(board,-1):
                return(10000000000, None)
            elif checkWinn(board,1):
                return(-10000000000, None)
            else:
                return(0,None)
        else:
            return(score_move(board,-1),None)
    if maximizingPlayer:
        value = -math.inf
        move = random.choice(valid_moves)
        for col in valid_moves:
            row = getNextEmptyRow(col,board)
            copy = board.copy()
            putPiece(row,col,-1,copy)
            score,_= minimax(depth-1,alpha,beta,False, copy)
            if score>value :
                value = score
                move = col
            alpha = max(alpha,value)
            if alpha >= beta:
                break
        return value,move
    else:
        value = math.inf
        move = random.choice(valid_moves)
        for col in valid_moves:
            row = getNextEmptyRow(col, board)
            copy = board.copy()
            putPiece(row,col,1,copy)
            score,_ = minimax(depth - 1 , alpha, beta, True,copy)
            if score<value:
                value = score
                move = col
            beta =  min(beta, value)
            if alpha >= beta:
                break
        return value, move


    

def pick_best_move(board, piece,location):
    
    valid_locations = get_valid_cols(board)
    best_score = -10000
    best_col = random.choice(valid_locations)
    if not validation(location,board):
        location = random.choice([0,1,2,3,4,5,6])
    temp_board1 = board.copy()
    row1 = getNextEmptyRow(location,board)
    putPiece( row1, location, piece,temp_board1)
    score1 = score_move(temp_board1, piece)
    for col in valid_locations:
        row = getNextEmptyRow(col,board)
        temp_board = board.copy()
        putPiece( row, col, piece,temp_board)
        score = score_move(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col
    if best_score<score1:
        best_score = score1
        best_col = location
    return best_col