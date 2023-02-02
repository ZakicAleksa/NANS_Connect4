#from multiplayer import *
from random import choice
import sys
import tkinter
import easygui
import plots
import multiplayer
import minimax
import AIwithRegression
from tk_html_widgets import HTMLLabel

if __name__ == "__main__":
    
    title = 'Connect4'
    text='Choose mode: minimax - legendary,  L1 - medium, L2 - easy'
    options = ['2 Players', 'Single player vs Minimax', 'Single player vs L1','Single player vs L2','Plot L1','Plot L2','About','Exit Game']
    flag=True
    while(flag):
        button=easygui.buttonbox(msg=text,title=title,choices=options,image='img_main.jpg')
        
        if button ==options[5]:
            plots.plot_L2()
        if button == options[4]:
            plots.plot_L1()
        if button == options[0]:
            multiplayer.init_multiplayer()
        if button == options[1]:
            minimax.init_minimax()
        if button == options[2]:
            AIwithRegression.init_regression(1)
        if button == options[3]:
            AIwithRegression.init_regression(2)
        if button == options[6]:
            root = tkinter.Tk()
            root.title("About")
            html_label = HTMLLabel(root, html='<html><div><h1>  Lasso(L1) and Ridge(L2) regression   </h1> <h4>Modovi Single player vs L1 i Single player vs L2  se zasnivaju na principima  regresije i regulacije.<br><br>L1(Lasso) i L2(Ridge) metode uvode pojam kaznene funkcije,izraz zvan penal,cime se koriguje izgled krive.<br><br>Na osnovu igranja protiv minmax algoritma, formira se dataSet, koji sluzi za treniranje L1 i L2 modela.Sto je dataSet veci,predikcija  kolone ce biti bolja.<br><br>Prilikom samog formiranja dataSeta,L1 i L2 modeli su prakticno nemocni,jer se regresija vrsi na malim skupom podataka.<br><br>Single player vs L1 je implemetiran u kombinaciji sa minimax algoritmom ciji je dept=1,gde se odlucuje koja je kolona bolja(dobijena lasso regresijom ili minmax algoritmom).Single player vs L2 je mod koji iskljucivo donosi odluku na osnovu ridge regresije. </h6> <h1>    MIN-MAX    </h1> <p> Minimax algoritam je rekurzivni algoritam koji za odredjen broj poteza bira onaj ciji je ishod nakon tog broja poteza najbolji.<br><br>U slucaju da je algoritmu prosledjena daleka buducnost, minimax ce sustinski uvek birati savsen potez.<br><br>Implementiran je minimax algoritam sa alpha-beta odsecanjem stabla,koji odseca onu stranu koja sigurno nece biti izabrana. Na taj nacin izbegavamo nepotrebno pretrazivanje vrednosti mimimax stabla. </h6> <h1>    Developers:   </h1> <p>Aleksa Zakic RA/79/2019<br><br>Djordje Vuckovic RA/8/2019')
            html_label.pack(fill="both", expand=True)
            html_label.fit_height()
            root.mainloop()
        if button == options[7]:
            flag=False
            sys.exit()
    
