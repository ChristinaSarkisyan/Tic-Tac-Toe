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

root = Tk()
root.title('Tik Tac Toe')

#make all the buttons
b1a = Button(root, text ="b1a", padx=50, pady=50, command=lambda: on_click("b1a"))
b1b = Button(root, text ="b1b", padx=50, pady=50, command=lambda: on_click("b1b"))
b1c = Button(root, text ="b1c", padx=50, pady=50, command=lambda: on_click("b1c"))
b2a = Button(root, text ="b2a", padx=50, pady=50, command=lambda: on_click("b2a"))
b2b = Button(root, text ="b2b", padx=50, pady=50, command=lambda: on_click("b2b"))
b2c = Button(root, text ="b2c", padx=50, pady=50, command=lambda: on_click("b2c"))
b3a = Button(root, text ="b3a", padx=50, pady=50, command=lambda: on_click("b3a"))
b3b = Button(root, text ="b3b", padx=50, pady=50, command=lambda: on_click("b3b"))
b3c = Button(root, text ="b3c", padx=50, pady=50, command=lambda: on_click("b3c"))


print("b1a",b1a)
#make title
title = Label(root, text = "Place your X", font =("arial", 15) , justify="center").grid(row=0, column=1)
   
buttons = [[b1a, b1b, b1c], [b2a, b2b, b2c],[b3a, b3b, b3c]]
np_buttons = np.array(buttons)
print("buttons: " , np_buttons)

for i in range(3):
    for j in range(3):
        np_buttons[i, j].grid(row=i+1, column=j)

root.mainloop()


brain = ans.Analysis('bl')
        
#have user interact with GUI
#update board
#display board

#repeat until someone has 3 in a row

#show congradulation message

