# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 00:01:01 2021

@author: chris
"""
import numpy as np

class Analysis():
    def __init__(self, type_a): #type_a is either 'bl' or 'bu' for builder or blocker
        self.board = np.zeros(shape = (3,3))
        #log = <file here>
        print("board:\n", self.board) #temp testor
        if type_a == 'bl': self.blocker()
        elif type_a == 'bu': self.builder()
        
    def blocker(self):
        #algorythm based on blocking the oponent goes here
        print("you are running blocker")
        #print(self.end_check())
    
    def builder(self):
        #algorythm based on building lines of 3
        print("you are running builder")
        #print(self.end_check())
    
    def update_log():
        print("log has been updated")
        
    def end_check(self):    #improve this to return message boxes and close the board
        if self.check_if_tie(): return "it was a tie!"
        if self.check_if_won('x'): return "you won"
        if self.check_if_won('o'): return "you lost"
        
    def check_if_won(self, player): #'x' for player, 'o' for cpu
        print("test")
        for i in self.board:
            if i == player:
                print("i fouund a ", player)
        #if player has 3 in a row, display "you won"
        #if cpu has 3 in a row, display "you lost
        #(if make multiplayer) if player 2 won, display "(name) won" and vice versa
   
    def check_if_tie(self):
        print("test")
        opens = 0
        # for i in self.board:
        #     if i != 0: opens +=1
            
        # if opens == 0: return True
        # else: return False
        #if all spaces taken, display "tie" message