#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 28-09-2023
# Last modification date: 10-10-2023
#--------------------------------------------------------------------------------------------------------

from cell import Cell
from position import Position
from utils.count import Count
from utils.selector import Selector

class Validation:
    
    #Class variable
    cause:str=""

    #Validate if a move is allowed by combining other constraints
    def moveIsAllowedAhead(playerPosFinal,board):
     
       
       #isNotTowardsAWall, isNotTowardsAFireWithOutWater= False,False
       isAvailable=False
       isInsideBorders:bool = Validation.isInsideBorders(playerPosFinal,board.getRowsNum(),board.getColumsNum())
       if isInsideBorders:
           isAvailable = Validation.__isAvailable(board.getCell(playerPosFinal))
        #isNotTowardsAWall = Validation.__isNotTowardsAWall(board.getCell(agentPosFinal))
        #isNotTowardsAFireWithOutWater = Validation.__isNotTowardsAFireWithOutWater(board.getCell(agentPosFinal),agent.getBucket().getLoad())
       #return isInsideBorders and isNotTowardsAWall and isNotTowardsAFireWithOutWater
       return isInsideBorders and isAvailable
    
    def moveIsAllowedBack(playerPosFinal,board):
     
       
       isInsideBorders:bool = Validation.isInsideBorders(playerPosFinal,board.getRowsNum(),board.getColumsNum())
       #if isInsideBorders:
       #    isAvailable = Validation.__isAvailable(board.getCell(playerPosFinal))
        #isNotTowardsAWall = Validation.__isNotTowardsAWall(board.getCell(agentPosFinal))
        #isNotTowardsAFireWithOutWater = Validation.__isNotTowardsAFireWithOutWater(board.getCell(agentPosFinal),agent.getBucket().getLoad())
       #return isInsideBorders and isNotTowardsAWall and isNotTowardsAFireWithOutWater
       return isInsideBorders
    
   
    def __isAvailable(cell:Cell):
        return (cell.isAvailable())


    #Validate if a move is inside the board       
    def isInsideBorders(pos: Position, rows:int, columns:int):
        validate = (pos.getCordI()in range(0,rows)) and (pos.getCordJ() in range (0,columns))
        if not(validate): 
            __class__.cause= "Border"
        return validate
    
    #Validate if the three achive the specific level
    def isTurnGoal(finalDeep, actualDeep ):
        
        return actualDeep > finalDeep #REVISAR

    def thereIsACoin(cell):
        return  cell.getNumber() == 1 or cell.getNumber() == 3

    def isGameGoal(board):

        #print("FUEGOS ENCENDIDOS: ",count)
        return Count.availableCoins(board)== 0
    
    def getCause():
        return __class__.cause
    
    def canReturn(preValues, actValues):
   
        difAvaCoins = False
        if preValues !={} and actValues != {}:
       
            difAvaCoins = preValues["coins"] != actValues["coins"]
            #print("COINS: ", preValues["coins"], " ", actValues["coins"])
           
        return difAvaCoins 
    
    def listFullChecked(counter,aList):
        return (counter+2 == len(aList) + 1) or (counter+2 == len(aList))
    

    def validateGameResult(scoreHuman, scoreMachine, gameScore)->str:
       result = ""
       if abs(scoreHuman-scoreMachine) > abs(gameScore - (scoreHuman+scoreMachine)):
           result+="¡Win: "
           if(scoreHuman> scoreMachine):
               result+="Red Yoshi!"
           if(scoreMachine> scoreHuman):
               result+="Green Yoshi!"
       elif abs(scoreHuman-scoreMachine)==0 and abs(gameScore - (scoreHuman+scoreMachine))==0:
           result+= "¡Draw!"
       else:
           result+="¡Compiting!"
    
       return result
    
           
           
           
    
    