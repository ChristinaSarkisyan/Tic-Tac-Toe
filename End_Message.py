# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 16:26:07 2021

@author: chris
"""

from tkinter import *
import Board

class End_Message:
    def __init__(self, end):
        root = Tk()
        root.title('Tik Tac Toe')
        # root.geometry("300x200")
        # root.maxsize(300, 200)
        
        
        self.title = Label(root, text = end, font =("arial", 15) , justify="center")
        
        self.b1 = Button(root, text = "Quit", command= root.destroy)
        self.b2 = Button(root, text = "Play Again", command= root.destroy)
        
        self.title.grid(row=0, column=1)
        self.b1.grid(row=1, column=1)
        self.b2.grid(row=2, column=1)
        
        root.mainloop()