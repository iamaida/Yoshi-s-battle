#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 2
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 26-09-2023
# Last modification date: 17-11-2023
#--------------------------------------------------------------------------------------------------------


from board import Board


class Player:

    #Constructor
    def __init__(self,  properties:dict):

        # Instance attribute
        self.properties=properties 
      
        
    def getPos(self):
        return self.properties["position"]
    
    def getNumber(self):
        return self.properties["number"]
    
    def getName(self):
        return self.properties["name"]
    
    def getScore(self):
        return self.properties["score"]
    
    
    def addScore(self, score):
        self.properties["score"]+= score
    
    def subtractScore(self, score):
        self.properties["score"]-= score
    
    def __findPosition(self, board:Board) -> None:
        
        for row in board:
            for cell in row:
     
                if cell.getNumber() == self.properties["number"]:
                    self.properties["position"] = cell.getPosition()
                    break
        
    
    def getPosition(self, board:Board):
        self.__findPosition(board)
        return self.properties["position"]
    
   