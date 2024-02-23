#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 26-09-2023
# Last modification date: 26-09-2023
#--------------------------------------------------------------------------------------------------------
from position import Position
from cell import Cell


class Selector:

   
    def chooseColor(num:int) -> str:
        colors ={0:"#FCFCFC", 1:"#F3F30C",
                 3:"#0C87F3",4:"#355E3B",5:"#C0392B"}
        return colors[num]
    
    def choosePosition(orientation, player, board) ->str:
        agentActalPos: Position = player.getPosition(board.get())
        positions ={"up-right":Position(agentActalPos.getCordI() - 2, agentActalPos.getCordJ()+1),
                    "up-left":Position(agentActalPos.getCordI() - 2, agentActalPos.getCordJ()-1),
                    "down-right":Position(agentActalPos.getCordI() + 2, agentActalPos.getCordJ()+1),
                    "down-left":Position(agentActalPos.getCordI() + 2, agentActalPos.getCordJ() -1),
                    "left-up":Position(agentActalPos.getCordI()-1, agentActalPos.getCordJ()-2),
                    "left-down":Position(agentActalPos.getCordI()+1, agentActalPos.getCordJ()-2),
                    "right-up": Position(agentActalPos.getCordI()-1, agentActalPos.getCordJ()+2),
                    "right-down": Position(agentActalPos.getCordI()+1, agentActalPos.getCordJ()+2)}
        return positions[orientation]
    

    
    def chooseNewPosition(orientation, agentActalPos) ->str:
        positions ={"up":Position(agentActalPos.getCordI() - 1, agentActalPos.getCordJ()),
                    "down":Position(agentActalPos.getCordI() + 1, agentActalPos.getCordJ()),
                    "left":Position(agentActalPos.getCordI(), agentActalPos.getCordJ()-1),
                    "right": Position(agentActalPos.getCordI(), agentActalPos.getCordJ()+1)}
        return positions[orientation]
    
    def reverseOrientation(orientation) ->str:
        positions ={"up-right":"down-left",
                    "up-left":"down-right",
                    "down-right":"up-left",
                    "down-left":"up-right",
                    "left-up":"right-down",
                    "left-down":"right-up",
                    "right-up":"left-down",
                    "right-down":"left-up",
                     None:"" }
        return positions[orientation]
    

    def chooseName(num:int) -> str:
        names ={0:"free", 1:"normal start",
                3:"special start", 4:"green yoshi",
                5:"red yoshi"}
        return names[num]
    
    def findPlayer(num:int) -> bool:
        boolValue = False
        if num in range(4,6):
            boolValue=True
        return boolValue
    
    def createCell(i:int, j:int, num:int) -> Cell:
        properties = {
                    "position": Position(i,j),
                    "number": num,
                    "color": Selector.chooseColor(num),
                    "name": Selector.chooseName(num),
                    "available":True,
                    "playerHere": Selector.findPlayer(num)}
    
        return Cell(properties)
    

   
    