# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:58:55 2021

@author: chris
"""

#import Board
import Message
import tkinter as tk
import Board as bd

#get message running
root = tk.Tk()
root.geometry("300x200")
root.maxsize(300, 200)
root.title('Tik Tac Toe')
app = Message.Message(master=root)


app.mainloop()


root1 = tk.Tk()
root1.geometry("600x600")
root1.maxsize(600, 600)
root1.title('Tik Tac Toe')
game = bd.Board(master=root1)
game.mainloop()