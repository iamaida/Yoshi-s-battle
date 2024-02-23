#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 26-09-2023
# Last modification date: 09-10-2023
#--------------------------------------------------------------------------------------------------------
from board import Board
#from agent import Agent
from position import Position
from cell import Cell
from utils.validation import Validation
from utils.printer import Printer
from utils.selector import Selector

class Move:
    
    direction:str =""
    failMessag:str =""

    #Move agent to the position indicate by the orientation
    def toward(orientation, player, board):
        playerPosFinal: Position = Selector.choosePosition(orientation, player, board)
        __class__.direction =orientation
        Move.goAhead( playerPosFinal,board,player)
    
    #Move agent to the opposite position indicate by the orientation
    def back(orientation,player, board):
        playerActalPos: Position = player.getPosition(board.get())
        #####
        #print("---CELL INFO---")
        #Printer.showCellInfo(state.getBoard().getCell(agentActalPos))
        ####
        if board.getCell(playerActalPos).getNumber()!=player.getNumber():
            
            playerPosFinal: Position = Selector.choosePosition(Selector.reverseOrientation(orientation), player, board)
            __class__.direction ="Reverse "+Selector.reverseOrientation(orientation)
            Move.__goBack( playerActalPos,playerPosFinal,board,player)
        else:

            player.subtractScore(player.getScore())
            for cell in board.getCoinsCells():
                cell.enable()
            board.getCell(playerActalPos).removePlayerFromHere()


    #Switch the value of isAgentHere propertie depents of agent final position
    def __changePlayerPosition(playerPosFinal,player,board:Board):
        playerPosInit: Position = player.getPosition(board.get())
        initCell: Cell = board.getCell(playerPosInit)
        initCell.removePlayerFromHere()
        initCell.enable()
        finalCell: Cell = board.getCell(playerPosFinal)
        finalCell.changePlayerToHere()
        finalCell.disable()
       
    
    #Switch the value of isAgentHere propertie depents of agent final position
    def __changeAgentPositionBack(playerActalPos,playerPosFinal,player, board):
        #agentPosInit: Position = agent.getPosition(board.get())
        initCell: Cell = board.getCell(playerActalPos)
        #initCell.changeAgentHere()
        initCell.removePlayerFromHere()
        initCell.enable()
        finalCell: Cell = board.getCell(playerPosFinal)
        #finalCell.changeAgentHere()
        finalCell.changePlayerToHere()
        finalCell.disable()
        #Printer.showMessage(f'Move Back: {__class__.direction} ')
        #print("CAMBIO POSICIÓN BACK-----")

    #Execute a valid agent move ahead
    def goAhead(playerPosFinal,board:Board,player):
        
        
        if Validation.moveIsAllowedAhead(playerPosFinal,board):
            
            Move.__changePlayerPosition(playerPosFinal,player, board)
            #print("Player: ",player.getName())
            if Validation.thereIsACoin(board.getCell(playerPosFinal)):
                
                player.addScore(board.getCell(playerPosFinal).getNumber())
                #print(player.getName(), player.getScore())

        else:
            __class__.failMessag ="not allowed"
            #Printer.showMessage(f'¡{Validation.getCause()}:Move {__class__.direction} is {__class__.failMessag}!')
    
    #Execute a valid agent move back

    def __goBack(playerActalPos,playerPosFinal,board:Board,player):
       
         #print("POR AQUI: Posicion final: ",agentPosFinal.getCordI()," ",agentPosFinal.getCordJ() , " ", Validation.moveIsAllowedBack(agentPosFinal,agent,board))
         if Validation.moveIsAllowedBack(playerPosFinal,player,board):
            Move.__changeAgentPositionBack(playerActalPos,playerPosFinal,player, board)
            if Validation.thereIsACoin(board.getCell(playerActalPos)):
              board.getCell(playerActalPos).enable()
              player.subtractScore(board.getCell(playerActalPos).getNumber())
         else:
            #print("POR AQUI: Posicion final: ",agentPosFinal.getCordI()," ",agentPosFinal.getCordJ() , " ", not(Validation.moveIsAllowedBack(agentPosFinal,agent,board)) and Validation.moveIsAllowedBack(agentPosInit,agent,board))
            if not(Validation.moveIsAllowedBack(playerPosFinal,player,board)) and Validation.moveIsAllowedBack(playerActalPos,player,board):
                initCell: Cell = board.getCell(playerActalPos)
                initCell.changePlayerToHere()
                #Printer.showMessage(f'Move Back: {__class__.direction} ')
                if Validation.thereIsACoin(board.getCell(playerActalPos)):
                    board.getCell(playerActalPos).enable()
                    player.subtractScore(board.getCell(playerActalPos).getNumber())
            else:
                __class__.failMessag ="not allowed"
          

         
            #Printer.showMessage(f'¡{Validation.getCause()}:Move {__class__.direction} is {__class__.failMessag}!')
