#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 1
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 30-09-2023
# Last modification date: 09-10-2023
#--------------------------------------------------------------------------------------------------------
import math
from board import Board
#from agent import Agent
from node import Node
from state import State
from utils.validation import Validation
from utils.printer import Printer
from move import Move
from utils.count import Count
from utils.selector import Selector
import time

#Breadth First Search
class BFS:
    #expande(Node)
    queue:list =[]
    terminal_nodes: list =[]
    utilities: list =[]
    countExpandedNodes:int=1
    treeDeep:int=0
    computingTime:float =0.0
    finalNode= None
    name="BFS"
    final_node=[]
    final_id=0
    
    
    def search(board:Board, playerMachine, playerHuman,operators, level):
       
        print("------ ",__class__.name," ------")
        #Printer.showBoardDetails(board.get())
        state = State(board,playerMachine, playerHuman)
        #state:State, father:'Node', operator:str, deep:int, cost:int
        father = Node(state, None,None,0,0)

        print("Father")
        Printer.showNodeInfo(father)
  
        
        isGoal =Validation.isTurnGoal(level, father.getDeep())
      
      
        while(not(isGoal)):
          
            BFS.generateCandidateNodes(operators,father)    
                
            BFS.moveBack(father)
     
           
            if len(__class__.queue) > 0:
                isGoal = Validation.isTurnGoal(level, __class__.queue[0].getDeep())
            else:
                 isGoal = True
            
            actualLevel = father.getDeep()
            
            if(not(isGoal)):
                 father=__class__.queue[0]
                 #print("Father")
                 #Printer.showNodeInfo(father)
                 __class__.countExpandedNodes+=1
                 newLevel = father.getDeep()
                 BFS.moveToward(father)
                 if actualLevel != newLevel:
                      __class__.terminal_nodes.clear()
                      __class__.utilities.clear()
                 #if father.getDeep() == level:
                 __class__.terminal_nodes.append(father)
                 __class__.utilities.append(BFS.utility(father))
                 __class__.queue.pop(0)
            else:
                
                #print("FINAL!!!")
                BFS.moveBack(father)
                __class__.queue.clear()
            
            
        
    def getExpandedNodes():
         return __class__.countExpandedNodes
    
    def getTreeDeep():
         return __class__.treeDeep
    
    def getComputingTime():
         return __class__.computingTime
    
    def getPath():
         return BFS.findPath(__class__.finalNode,"reverse")

    def generateCandidateNodes(moveCand,father):
        listofMoves = list(moveCand.split(","))

        player = BFS.choosePlayer(father)
        board = father.getState().getBoard()
        for operator in listofMoves:
            if Validation.moveIsAllowedAhead(Selector.choosePosition(operator, player, board),board):
                BFS.createNodes(operator, father)

    def createNodes(operator, father):
         node = Node(father.getState(), father, operator, father.getDeep()+1,0)
         __class__.queue.append(node)
 
   
    def findNodePath(node, form):
            dirNodes =[]
            while(node.getFather() != None):
                dirNodes.append(node)
                node = node.getFather()
            if form == "reverse":
                dirNodes.reverse()
            return dirNodes
    

    def findPath(node, form):
            directios =[]
            if node != None:
                while(node.getFather() != None):
                    directios.append(node.getOperator())
                    node = node.getFather()
                if form == "reverse":
                 directios.reverse()
            return  directios
    
    def moveBack(node):
           dirNodes = BFS.findNodePath(node, "unreverse")
           for item in dirNodes:
               player = BFS.choosePlayerToward(item)
               Move.back(item.getOperator(), player, item.getState().getBoard())
    
    def moveToward(node):
            dirNodes = BFS.findNodePath(node, "reverse")
            for item in dirNodes:
               
               player = BFS.choosePlayerToward(item)
               #print("Father Deep: ",item.getDeep()-1, "player: ", player.getName())
               Move.toward(item.getOperator(), player, item.getState().getBoard())

    def choosePlayer(father):
         player = father.getState().getPlayerMachine()
         if((father.getDeep() % 2)!=0):
             player = father.getState().getPlayerHuman()

         return player
    
    def choosePlayerToward(father):
         
         if((father.getDeep()-1 % 2)==0):
             player = father.getState().getPlayerMachine()
         else:
             player = father.getState().getPlayerHuman()
             

         return player
              
    def getScores(node):
         scorePlayerMachine = node.getState().getPlayerMachine().getScore()
         scorePlayerHuman = node.getState().getPlayerHuman().getScore()
         return {"machine":scorePlayerMachine, "human":scorePlayerHuman}
    
    
    def utility(node):
         scores = BFS.getScores(node)
         #print("score machine = ",scores["machine"])
         #print("score human =",scores["human"])
         value = 0
         if scores["machine"] > scores["human"]:
              value = scores["machine"]
         elif scores["machine"] < scores["human"]:
              value = -scores["human"]
         #print(value)
         return value
     
    def minmax():
         #i = 0
         __class__.final_node.clear()
         __class__.final_id=0
         print("1. Utilidades")
         print(__class__.utilities)
         level =__class__.terminal_nodes[len(__class__.terminal_nodes)-1].getDeep()

         aLevel = level
         while (aLevel >= 0):
      
              operator = __class__.terminal_nodes[0].getFather().getOperator()
              i=0
              new_util =[]
              
              while(operator == __class__.terminal_nodes[0].getFather().getOperator()):
                   
            
                   new_util.append(__class__.utilities[i])
                   if(operator==None):
                        __class__.final_node.append(__class__.terminal_nodes[i])
           
                   i+=1
                   if (i == len(__class__.terminal_nodes)):
                        __class__.terminal_nodes.append( __class__.terminal_nodes[len(__class__.terminal_nodes)-1].getFather())
                        operator = 'Final'
                   else:   
                         operator = __class__.terminal_nodes[i].getFather().getOperator()
                         if(operator != __class__.terminal_nodes[0].getFather().getOperator()):
                          __class__.terminal_nodes.append( __class__.terminal_nodes[0].getFather())
                   
             
              if(__class__.terminal_nodes[len(__class__.terminal_nodes)-1].getOperator() == None):
                   #print("Entró por aqui")
                   while(len(__class__.utilities)>0):
                     __class__.utilities.pop(0)
                     __class__.terminal_nodes.pop(0)
              else:
                    goal= i+1
                    while(i < goal):
                         
                         __class__.utilities.pop(0)
                         __class__.terminal_nodes.pop(0)
                         i+=1
                
              
              
              if aLevel == 0:
                  result =BFS.getNewUtilityWithDeep(new_util, aLevel)
                  __class__.utilities.append(result["value"])
                  __class__.final_id =result["id"]
                  
              else:
                  __class__.utilities.append(BFS.getNewUtility(new_util, aLevel)) 
                   
              
              aLevel = __class__.terminal_nodes[0].getDeep() -1
              
      

    def getMachineMove():
         return __class__.final_node[__class__.final_id].getOperator()
    
    def getFinalUtility():
         return __class__.utilities
    def getNewUtility(listOfnumbers, deep):
        
          value = max(listOfnumbers)
          if(deep % 2 !=0):
               value = min(listOfnumbers)  
          
          return value
    
    def getNewUtilityWithDeep(listOfnumbers, deep):
          
          value = max(listOfnumbers)
          id = listOfnumbers.index(value)
          if(deep % 2 !=0):
               value = min(listOfnumbers)
               id = listOfnumbers.index(value)
   
          return {"value":value, "id":id}

    def reset():
         __class__.utilities.clear()
         __class__.final_node.clear()
         __class__.terminal_nodes.clear()
          

              
              
