#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 26-09-2023
# Last modification date: 17-11-2023
#--------------------------------------------------------------------------------------------------------



from utils.worldgenerator import WorldGenerator
from utils.printer import Printer
from board import Board
from player import Player
from position import Position
from bfs import BFS



def main():
    WorldGenerator.execute()
    Printer.showBoardNumbers(WorldGenerator.getOutput())
    operators="up-right,up-left,down-right,down-left,left-up,left-down,right-up,right-down"
    aBoard = Board(WorldGenerator.getOutput())
    aBoard.setup()
    #Printer.showBoardDetails(aBoard.get())
    playerMachine = Player(properties={"position":Position(-1,-1),"number":4,"name":"green yoshi","score":0})
    playerHuman = Player(properties={"position":Position(-1,-1),"number":5, "name":"red yoshi","score":0})
    level = 6
    Printer.showPlayerInfo(playerMachine, aBoard.get())
    Printer.showPlayerInfo(playerHuman, aBoard.get())
    BFS.search(aBoard, playerMachine, playerHuman, operators,level)
    BFS.minmax()
    print("Machine Move: ",BFS.getMachineMove()) 
    print("Final Utility", BFS.getFinalUtility())



   
    

    
    
main()