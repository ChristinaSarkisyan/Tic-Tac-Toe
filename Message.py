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
        self.button = Button(root, text = "Start")
        
        self.title.grid(row=0, column=1)
        self.subtitle.grid(row=1, column=1)
        self.button.grid(row=2, column=1)
        
        root.mainloop()
        #button
# class Message(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
       
        #these arent showing u for some readon!
    # def create_widgets(self):
    #     self.message = tk.Label(text= "hi", width = 20, height = 20)
        # self.greeting = tk.Button(self)
        # self.greeting["text"] = "Start Game\n(click me)"
        # self.greeting["command"] = self.open_board()
        # self.greeting.pack(side="top")
    
        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")
       
        
       # self.message = tk.Label(text= "hi", width = 20, height = 20)
        # self.button = tk.Button(text="Continue", width=15, height=5)
        # self.message.pack()
        # self.create_widgets()
    
        
# class Message(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.quit = tk.Button(self, text="Start", command=self.master.destroy)
#         self.quit.pack(side="bottom")

#     def test(self):
#         print("button was pressed")
#         #add a timer here or a thing to wait for widget to stop?
#         #self.open_board()
# #gets board running        
    # def open_board(self):
    #         root1 = tk.Tk()
    #         root1.geometry("600x600")
    #         root1.maxsize(600, 600)
    #         root1.title('Tik Tac Toe')
    #         game = Board.Board(master=root1)
    #         game.mainloop()