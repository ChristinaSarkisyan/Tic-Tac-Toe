# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:46:06 2021

@author: chris
"""
from tkinter import *
import Board

class Message:
    def __init__(self):
        root = Tk()
        root.title('Tik Tac Toe')
        # root.geometry("300x200")
        # root.maxsize(300, 200)
        
        
        self.title = Label(root, text = "Tic Tac Toe", font =("arial", 15) , justify="center")
        self.subtitle= Label(root, text="The Game", justify="center")
        self.button = Button(root, text = "Start", command= root.destroy)
        
        self.title.grid(row=0, column=1)
        self.subtitle.grid(row=1, column=1)
        self.button.grid(row=2, column=1)
        
        root.mainloop()
        
 