# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:46:06 2021

@author: chris
"""
import tkinter as tk


class Message():
    def __init__(self):
        print("you made a message")
        self.popup = tk.Tk()
        self.message = tk.Label(text= "hi", width = 20, height = 20)
        self.button = tk.Button(text="Continue", width=15, height=5)
        self.message.pack()
        
        self.popup.mainloop()
        