# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:06:54 2021

@author: chris
"""

from tkinter import *
import Analysis as ans
import numpy as np


class Board():
    def __init__(self):
        self.buttons = []
        root = Tk()
        root.title('Tik Tac Toe')
        #make all the buttons
        for i in range(3):
            for j in range(3):
                self.buttons.append(Button(root, text ="", padx=50, pady=50)) #add padding
        
        #make title
        self.title = Label(root, text = "Place your X", font =("arial", 15) , justify="center")
       
        #put them into the window
        for i in range(3):
            for j in range(3):
                self.buttons[i + (j*3) - 1].grid(row=i+1, column=j)
        self.title.grid(row=0, column=1)
        root.mainloop()
        
        
        
        #brain = ans.Analysis('bl')
        
    # def create_widgets(self):
    #     for i in range(3):
    #         for j in range(3):
    #             self.buttons[i][j] = tk.Button(self)#, text ="testing", padx=50, pady=50)
        
    #     print("buttons after create widget\n", self.buttons, "\n\n") #temp testor
    #     # self.buttonsButton(self)
    #     # self.greeting["text"] = "welcome to boarddd"
    #     #self.greeting.pack(side="top")
        
    #     for i in self.buttons:
    #          i.pack()
    
        
        
        
    # def update_board ():
    #     print("test")
    #     #reads new input from user and updates board object to match
        
    # def return_board():
    #     print("test")
        
        
    # def show_board():
    #     print("test")
        
        
    # def disable_buttons():
    #     print("buttons disabled")