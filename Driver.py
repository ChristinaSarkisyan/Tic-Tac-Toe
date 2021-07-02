# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:14:58 2021

@author: chris
"""
from tkinter import *
import Board as bd
import Message as msg
import Analysis as ans
import numpy as np
import Board_Minder as bm

def on_click():
    print("you clicked a button")

msg.Message()
#bd.Board()
buttons = []
root = Tk()
root.title('Tik Tac Toe')
#make all the buttons
for i in range(3):
    for j in range(3):
        buttons.append(Button(root, text ="", padx=50, pady=50, command= on_click )) 

#make title
title = Label(root, text = "Place your X", font =("arial", 15) , justify="center")
   
#put them into the window
for i in range(3):
    for j in range(3):
        buttons[i + (j*3) - 1].grid(row=i+1, column=j)
title.grid(row=0, column=1)
root.mainloop()


brain = ans.Analysis('bl')
        
#have user interact with GUI
#update board
#display board

#repeat until someone has 3 in a row

#show congradulation message

