#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 2
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 17-11-2023
# Last modification date: 17-11-2023
#--------------------------------------------------------------------------------------------------------
from utils.selector import Selector
from position import Position
from utils.validation import Validation
from utils.printer import Printer

class Board:

    grid:list = []
    coins:list = []

    def __init__(self, template:list):
        self.template=template

    def setup(self) -> None:

        boardRow:list =[]
      
        for i,row in enumerate(self.template):
          
            for j,num in enumerate(row):
                cell= Selector.createCell(i,j,num)
                boardRow.append(cell)
                if num==1 or num==3:
                    __class__.coins.append(cell)
                if num==5 or num==4:
                    cell.disable()
                    
            __class__.grid.append(boardRow)
            boardRow=[]
               
    def get(self)-> list:
        return __class__.grid
    
    def set(self, initBoard)-> list:
        __class__.grid = initBoard
    
    def getRowsNum(self)-> list:
        return len(__class__.grid)
    
    def getColumsNum(self)-> list:
        return len(__class__.grid[0])
    
    def getCell(self,pos: Position) -> None:
        
        if Validation.isInsideBorders(pos, self.getRowsNum(), self.getColumsNum()):
            return __class__.grid[pos.getCordI()][pos.getCordJ()]
        else:
            Printer.showMessage('¡Cell no available!')

    def getCoinsCells(self) -> list:
        return __class__.coins
    
    def reset(self):
        __class__.grid=[]
        __class__.coins=[]

    def getPosition(self,number, environment):
        pos ={}
        for i in range(0, len(environment)):
            for j in range(0, len(environment[0])):

                    if (environment[i][j] == number):
                        pos["i"]=i
                        pos["j"]=j
        return pos




 