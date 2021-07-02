# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:06:54 2021

@author: chris
"""

import tkinter as tk
import Analysis as ans

class Board(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        
        brain = ans.Analysis('bl')
        
    def create_widgets(self):
        self.greeting = tk.Button(self)
        self.greeting["text"] = "welcome to boarddd"
        self.greeting.pack(side="top")
    
        
        
        
    def update_board ():
        print("test")
        #reads new input from user and updates board object to match
        
    def return_board():
        print("test")
        
        
    def show_board():
        print("test")
        
    