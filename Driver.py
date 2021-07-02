# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:14:58 2021

@author: chris
"""

import Board as bd
import tkinter as tk
import Message as msg


#display a message
root = tk.Tk()
root.geometry("300x200")
root.maxsize(300, 200)
root.title('Tik Tac Toe')
app = msg.Message(master=root)

app.mainloop()

#find a way to wait till app ends to start the rest
#make a board
root1 = tk.Tk()
root1.geometry("600x600")
root1.maxsize(600, 600)
root1.title('Tik Tac Toe')
game = bd.Board(master=root1)
game.mainloop()

#have user interact with GUI
#update board
#display board

#repeat until someone has 3 in a row

#show congradulation message