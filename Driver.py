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

def on_click(code):
    print("you clicked a button ", code)
    #self.state =DISABLED

msg.Message()
#bd.Board()
buttons = []
root = Tk()
root.title('Tik Tac Toe')

#make all the buttons
b1a = Button(root, text ="b1a", padx=50, pady=50, command=lambda: on_click("b1a")).grid(row=1, column=0)
b1b = Button(root, text ="b1b", padx=50, pady=50, command=lambda: on_click("b1b")).grid(row=1, column=1)
b1c = Button(root, text ="b1c", padx=50, pady=50, command=lambda: on_click("b1c")).grid(row=1, column=2)
b2a = Button(root, text ="b2a", padx=50, pady=50, command=lambda: on_click("b2a")).grid(row=2, column=0)
b2b = Button(root, text ="b2b", padx=50, pady=50, command=lambda: on_click("b2b")).grid(row=2, column=1)
b2c = Button(root, text ="b2c", padx=50, pady=50, command=lambda: on_click("b2c")).grid(row=2, column=2)
b3a = Button(root, text ="b3a", padx=50, pady=50, command=lambda: on_click("b3a")).grid(row=3, column=0)
b3b = Button(root, text ="b3b", padx=50, pady=50, command=lambda: on_click("b3b")).grid(row=3, column=1)
b3c = Button(root, text ="b3c", padx=50, pady=50, command=lambda: on_click("b3c")).grid(row=3, column=2)

#make title
title = Label(root, text = "Place your X", font =("arial", 15) , justify="center").grid(row=0, column=1)
   

root.mainloop()


brain = ans.Analysis('bl')
        
#have user interact with GUI
#update board
#display board

#repeat until someone has 3 in a row

#show congradulation message

