
from random import random
from matplotlib import pyplot as plt
import numpy as np
import math
import random
from pygame.constants import RESIZABLE
from sympy import true
import constant as const
import pygame as pg
import sys
from regression import *
import serialization 
import pandas as pd

def plot_L2():
    x,y=serialization.read()
    x=sorted(x)
    data = pd.DataFrame(np.column_stack([x,y]),columns=['x','y'])
    for i in range(2,16):
        name = 'x_%d'%i
        data[name]=data['x']**i
    print(data.head())
    predictors = ['x']
    predictors.extend(['x_%d'%i for i in range(2,16)])

    #When alpha=0 we have linear regression
    alpha_ridge = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2,0, 1, 5, 10, 20]
    col_ = ['rss','intercept'] + ['coef_x_%d'%i for i in range(1,16)]
    ind = ['alpha_%.2g'%alpha_ridge[i] for i in range(11)]
    coef_matrix_ridge = pd.DataFrame(index=ind, columns=col_)
    models_to_plot = {1e-10:231, 1e-8:232, 1e-4:233, 1e-3:234, 1e-2:235,5:236}
    for i in range(11):
        coef_matrix_ridge.iloc[i,] = ridge_regression_plot(data, predictors, alpha_ridge[i],models_to_plot)
    plt.show()

def plot_L1():
        x,y=serialization.read()
        x=sorted(x)
        data = pd.DataFrame(np.column_stack([x,y]),columns=['x','y'])
        for i in range(2,16):
            name = 'x_%d'%i
            data[name]=data['x']**i
        print(data.head())
        predictors = ['x']
        predictors.extend(['x_%d'%i for i in range(2,16)])
    
        #When alpha=0 we have linear regression
        alpha_lasso = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2,0, 1, 5, 10, 20]
        col_ = ['rss','intercept'] + ['coef_x_%d'%i for i in range(1,16)]
        ind = ['alpha_%.2g'%alpha_lasso[i] for i in range(11)]
        coef_matrix_lasso = pd.DataFrame(index=ind, columns=col_)
        models_to_plot = {1e-15:231, 1e-10:232, 1e-4:233, 1e-3:234, 1e-2:235, 5:236}
        for i in range(11):
            coef_matrix_lasso.iloc[i,] = lasso_regression_plot(data, predictors, alpha_lasso[i],models_to_plot)
        plt.show()