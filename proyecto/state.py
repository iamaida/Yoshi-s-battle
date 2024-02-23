#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 30-09-2023
# Last modification date: 30-09-2023
#--------------------------------------------------------------------------------------------------------

from board import Board
#from agent import Agent

class State:
    def __init__(self,board:Board, playerMachine, playerHuman):
        self.board = board
        self.playerMachine = playerMachine
        self.playerHuman = playerHuman

    def getBoard(self):
        return self.board
    
    def getPlayerMachine(self):
        return self.playerMachine
    
    def getPlayerHuman(self):
        return self.playerHuman
    
  