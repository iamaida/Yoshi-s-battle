#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 15-11-2023
# Last modification date: 15-11-2023
#--------------------------------------------------------------------------------------------------------

from utils.converter import Converter
from utils.selector import Selector
from utils.printer import Printer
from move import Move

class WorldGenerator:

    # class attribute
    world: list = []

  
    
    def __generateZeros2DArray(n) -> None:

        __class__.world = [[0 for i in range(n)] for j in range(n)]
        
        
    def __locateNormalCoins() -> None:
        normalCoinPosI, normalCoinPosJ = 0,0
        for iteration in range(1,5):

            __class__.world[normalCoinPosI][normalCoinPosJ] = 1
            __class__.world[normalCoinPosI][normalCoinPosJ+1] = 1
           

            if iteration == 1:
                __class__.world[normalCoinPosI+1][normalCoinPosJ] = 1
                normalCoinPosI, normalCoinPosJ = 0,len(__class__.world[0])-2
            elif iteration == 2:
                __class__.world[normalCoinPosI+1][normalCoinPosJ+1] = 1
                normalCoinPosI, normalCoinPosJ = len(__class__.world[0])-1,len(__class__.world[0])-2
            elif iteration == 3:
                __class__.world[normalCoinPosI-1][normalCoinPosJ+1] = 1
                normalCoinPosI, normalCoinPosJ = len(__class__.world[0])-1,0
            else:
                __class__.world[normalCoinPosI-1][normalCoinPosJ] = 1

    def __locateSpecialCoins() -> None:
             
             middlePos = (len(__class__.world[0])//2)-1
             specialCoinPosI, specialCoinPosJ = middlePos ,middlePos 
             __class__.world[specialCoinPosI][specialCoinPosJ] = 3
             __class__.world[specialCoinPosI][specialCoinPosJ+1] = 3
             __class__.world[specialCoinPosI+1][specialCoinPosJ] = 3
             __class__.world[specialCoinPosI+1][specialCoinPosJ+1] = 3
    
    def __locatePlayer(number) -> None:
        pos =Converter.generateRandomPos(0,len(__class__.world[0])-1)

        while(__class__.world[pos.getCordI()][pos.getCordJ()]in range(1, number)):

            pos =Converter.generateRandomPos(0,len(__class__.world[0])-1)
        
        __class__.world[pos.getCordI()][pos.getCordJ()] = number



    #Return the value of property world
    def getOutput() -> list:
        return __class__.world
    

    def execute()-> None:
        WorldGenerator.__generateZeros2DArray(8)
        WorldGenerator.__locateNormalCoins()
        WorldGenerator.__locateSpecialCoins()
        WorldGenerator.__locatePlayer(4)
        WorldGenerator.__locatePlayer(5)

    def updateInitPosition(player) -> None:
        for i in range(0, len(__class__.world)):
            for j in range(0, len(__class__.world[0])):
                if __class__.world[i][j] == player.getNumber():
                    __class__.world[i][j] = 0

    def updateFinalPosition(pos,player) -> None:
        
        __class__.world[pos.getCordI()][pos.getCordJ()] = player.getNumber()
                   

    def updateMachinePos(orientation, player, board):
        Move.goAhead(Selector.choosePosition(orientation, player, board),board,player)
        WorldGenerator.updateInitPosition(player)
        WorldGenerator.updateFinalPosition(Selector.choosePosition(orientation, player, board), player)

    def updateHumanPos(player, pos, board):
        Move.goAhead(pos,board,player)
        WorldGenerator.updateInitPosition(player)
        WorldGenerator.updateFinalPosition(pos, player)
        
        
          

 

       
      
     