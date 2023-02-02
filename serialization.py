"""
Modul u kome vrsimo iscitavanje podataka.
"""
import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def read():
    x = []
    y = []
    with open(r"dataSet.csv", 'r') as csvfile:
        read = csv.reader(csvfile, delimiter=',')
        next(read)
        for entitet in read:
            x.append(int(entitet[0]))
            y.append(int(entitet[1]))
        return x,y
        
def write(turn,column):
    with open('dataSet.csv','a',newline='') as csvfile:
        write = csv.DictWriter(csvfile,['Turn','Column'],delimiter=',')
        write.writerow({'Turn':turn+1,'Column': column}) 

def plot_dataSet():
    x,y=read()
    ax1 = plt.scatter(x,y,color='blue')
    plt.legend(labels=['Turn', 'Position'])
    plt.title('Linear regression', size=24)
    plt.xlabel('Turn', size=18)
    plt.ylabel('Position', size=18);
    plt.show()

