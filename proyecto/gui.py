#-----------------------------------------------------------------------------------------------
# Curso: Inteligencia Artificial
# Profesor: Oscar Bedoya
# Tema: Proyecto 2
# Nombre:Aida Milena Mina Caicedo
# Codigo: 1225328
# Fecha última modificación: 11-07-2022
#--------------------------------------------------------------------------------------------------------

from tkinter import*
import time

from utils.worldgenerator import WorldGenerator
from utils.printer import Printer
from utils.selector import Selector
from utils.validation import Validation
from board import Board
from player import Player
#from agent import Agent
from position import Position

from bfs import BFS
#from ucs import UCS
#from greedysearch import GreedySearch
#from astartsearch import AStartSearch

#---------------------------------------------------MAIN WINDOW PARAMETERS --------------------------
#Create main window
root = Tk()
#Title the window
root.title("Project 2")

#Set the geometry
#widht x height
root.geometry("995x635")

root.resizable(False, False)

root.configure(bg='white')

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------DATA---------------------------------------------

#Images
greenYoshiImage = PhotoImage(file = './images/GreenYoshi.png')
redYoshiImage = PhotoImage(file = './images/RedYoshi.png')

#Lists
#Search names
searchNames = ["BFS", "Uniform Cost", "DFS", "Greedy", "A*"]
searchResults = []
searchSelected= []
environment= []
vLevel = []
machineMove =[]

machinePoints =[0]
humanPoints =[0]
humanScore= StringVar()
machineScore = StringVar()
endResult = StringVar()




#Tkinter variable to radiobuttons
radioV= IntVar()
#Set radiobuttons with option 1 BFS like default option
radioV.set("1")
#Get current directory
#selection = StringVar()



#-------------------------------------------------------------------------------------------------
#----------------------------------------FRAMES CREATIONS---------------------------------------
#Create title frame
titleFrame = LabelFrame(root,highlightthickness=0, borderwidth=0, bg="black")# space about grid
titleFrame.pack() #space about window

#wFrame = LabelFrame(root,highlightthickness=0, borderwidth=0, bg="white")# space about grid
#wFrame.pack()

#Create main frame
mainFrame = Frame(root, padx=20, pady=10, width=500, height=150, bg="white")# space about grid
mainFrame.pack() #space about window

#Create world frame
worldFrame = LabelFrame(mainFrame, padx=20,pady=20,bg="black")# space about grid
worldFrame.grid(padx=10, pady=20, row=0, rowspan=60,column=0, columnspan=45) #space about window


playerOneScoreFrame = LabelFrame(mainFrame, padx=20,pady=20,bg="black")# space about grid
playerOneScoreFrame.grid(padx=10, pady=15, row=3, rowspan=15,column=45, columnspan=90) #space about window



playerTwoScoreFrame = LabelFrame(mainFrame, padx=20,pady=20,bg="black")# space about grid
playerTwoScoreFrame.grid(padx=10, row=18,rowspan=15,column=45, columnspan=90) #space about window


playButtonFrame = LabelFrame(mainFrame, padx=20,pady=20,bd=0)
playButtonFrame.grid(padx=10, row=31,rowspan=15,column=45, columnspan=90) 


playButton = Button(playButtonFrame, text="Play", font=("Consolas", 12, "bold"), command =lambda: showAnimation(), fg="white", bg="black", state=DISABLED)
playButton.pack()


ResultFrame = LabelFrame(mainFrame, padx=20,pady=20,bg="black")# space about grid
ResultFrame.grid(padx=10, row=43,rowspan=15,column=45, columnspan=100) #space about window

def chooseLevel(level):
    print(level)
    vLevel.clear()
    gameLevel = int(level[len(level)-1])
    if gameLevel == 1:
        vLevel.append(2)
    elif gameLevel == 2:
        vLevel.append(4)
    else:
        vLevel.append(6)


    machinePoints.clear()
    humanPoints.clear()
    machinePoints.append(0)
    humanPoints.append(0)
    humanScore.set("0   :")
    machineScore.set(":   0")
    endResult.set("¡Compiting!")
    WorldGenerator.execute()
    environment.clear()
    environment.append(WorldGenerator.getOutput())
    showWorld(environment[0])

    playButton.config(state=NORMAL)

def toggleMenu():

    def colapseToggleMenu():
        toggle_menu_fm.destroy()
        toggleButton.config(text="☰")
        toggleButton.config(command =lambda:toggleMenu())

    toggle_menu_fm = Frame(root, bg='black')

    levelOneButton = Button(toggle_menu_fm, text='Level 1',font=("Bold",15), bd=0, bg='black', fg='white', command =lambda:chooseLevel('Level 1'))
    levelOneButton.place(x=9,y=20)

    levelTwoButton = Button(toggle_menu_fm, text='Level 2', font=("Bold",15), bd=0, bg='black', fg='white', command =lambda:chooseLevel('Level 2'))
    levelTwoButton.place(x=9,y=60)

    levelThreeButton = Button(toggle_menu_fm, text='Level 3', font=("Bold",15), bd=0, bg='black', fg='white', command =lambda:chooseLevel('Level 3'))
    levelThreeButton.place(x=9,y=100)
    
    toggle_menu_fm.place(x=0, y=75, height=160, width=100)

    toggleButton.config(text="X")
    toggleButton.config(command =lambda:colapseToggleMenu())

toggleButton = Button(titleFrame, text="☰", font=("Bold", 25), command =lambda: toggleMenu(), fg="white",bg="black", bd = 0)
toggleButton.pack(side=LEFT)


#---------------------------------------------------------------------------------------------------



#-----------------------------------------TITLEFRAME WIDGETS--------------------------------------
#Show project title
def showGameTitle(title):
   titleLabel = Label(titleFrame, width= 75, height= 2, padx=7, pady=3,text= title,font=("Consolas", 20, "bold"),fg="white", bg="black")
   titleLabel.pack()


#-------------------------------------------------------------------------------------------------

#------------------------------------------OPTIONSFRAME WIDGET----------------------------------------
#Show  menu options
def showMenuOptions():

    emojiOne = Label(playerOneScoreFrame, width= 50, height= 61, padx=7, pady=3,image= greenYoshiImage,fg="black")
    emojiOne.grid(row=1,column=0, columnspan=4)
    #scoreOne
    #scoreOne

    machineScore.set(":   0")
    scoreOne = Label(playerOneScoreFrame, width= 10, padx=7, pady=3,textvariable=machineScore,font=("Consolas", 18, "bold"),fg="black")
    scoreOne.grid(row=1,column=4, columnspan=4)
    #emojiOne
    #emojiOne
    
    humanScore.set("0   :")
    scoreTwo = Label(playerTwoScoreFrame, width= 10, padx=7, pady=3,border=1,textvariable=humanScore,font=("Consolas", 18, "bold"),fg="black")
    scoreTwo.grid(row=2,column=0, columnspan=4)


    emojiTwo = Label(playerTwoScoreFrame, width= 50, height= 61, padx=7, pady=3,image= redYoshiImage,fg="black")
    emojiTwo.grid(row=2,column=4, columnspan=4)

    endResult.set(" ")
    resultLabel = Label(ResultFrame, width= 15, padx=7, pady=3,border=1,textvariable=endResult,font=("Consolas", 18, "bold"),fg="black")
    resultLabel .grid(row=1,column=0, columnspan=4)
    #scoreTwo.grid(row=2,column=4, columnspan=4)
    #emojiTwo.grid(row=2,column=0, columnspan=4)
    


#--------------------------------------------------------------------------------------------------
def moveHumanPlayer(row, col):
    print("Click on: ", row, ",", col)
    aBoard = Board(environment[0])
    aBoard.setup()
    posHuman =aBoard.getPosition(5,environment[0])
    playerHuman = Player(properties={"position":Position(posHuman["i"],posHuman["j"]),"number":5, "name":"red yoshi","score":0})
    WorldGenerator.updateHumanPos(playerHuman , Position(row,col),aBoard)
    
    environment.clear()
    environment.append(WorldGenerator.getOutput())
    aBoard = Board(environment[0])
    aBoard.setup()
    points = humanPoints[0]+ playerHuman.getScore()
    humanPoints.clear()
    humanPoints.append(points)
    print("Machine Human: ",humanPoints[0])
    print("Machine Machine: ",machinePoints[0])
    humanScore.set(str(humanPoints[0])+" :")
    machineScore.set(" : "+str(machinePoints[0]))
    endResult.set(Validation.validateGameResult(humanPoints[0], machinePoints[0], 24))
    showWorld(environment[0])
    aBoard.reset()

#---------------------------------------------------WORLDFRAME WIDGETS----------------------------------        
#Show world using Label widgets
def showWorld(environment:list)->None:
    
    
    #rows
    for i in range(len(environment)):
        #colums
        for j in range(len(environment[i])):
            #get cell number
    
            #Create label widget
            a_label = Button(worldFrame, padx=22, pady=17, bg= Selector.chooseColor(environment[i][j]), border=1, relief="solid", command= lambda row=i,col=j : moveHumanPlayer(row,col))
            #add label widget
            a_label.grid(row=i,column=j)

def showEmptyWorld()->None:
    
    
    #rows
    for i in range(8):
        #colums
        for j in range(8):
            #get cell number
    
            #Create label widget
            a_label = Button(worldFrame, padx=22, pady=17, bg= "#FCFCFC", border=1, relief="solid", command= lambda row=i,col=j : moveHumanPlayer(row,col))
            #add label widget
            a_label.grid(row=i,column=j)
    
    

            
          



#--------------------------------------------------------------------------------------------------

#--------------------------------------------BUTTONFRAME WIDGETS----------------------------------

#-------------------------------------------------------------------------------------------------
def showAnimation():
    '''
    showWorldNotExecute(environment[0])
    path=searchResults[0][4]
    showWorldAnimation(getPositions(environment[0], path),environment[0])
    '''
    machineMove.clear()
    #
    print("Botón pulsado el nivel es: ", vLevel[0])
    Printer.showBoardNumbers(environment[0])
    operators="up-right,up-left,down-right,down-left,left-up,left-down,right-up,right-down"
    aBoard = Board(environment[0])
    aBoard.setup()
    posMachine =aBoard.getPosition(4,environment[0])
    #Printer.showBoardDetails(aBoard.get())
    playerMachine = Player(properties={"position":Position(posMachine["i"],posMachine["j"]),"number":4,"name":"green yoshi","score":0})
    posHuman =aBoard.getPosition(5,environment[0])
    playerHuman = Player(properties={"position":Position(posHuman["i"],posHuman["j"]),"number":5, "name":"red yoshi","score":0})
    Printer.showPlayerInfo(playerMachine, aBoard.get())
    Printer.showPlayerInfo(playerHuman, aBoard.get())
    BFS.search(aBoard, playerMachine, playerHuman, operators,vLevel[0])
    BFS.minmax()
    machineMove.append(BFS.getMachineMove()) 
    print("Machine Move: ",machineMove[0])
    print("Final Utility", BFS.getFinalUtility())
  
    posMachine =aBoard.getPosition(4,environment[0])
    #Printer.showBoardDetails(aBoard.get())
    playerMachine = Player(properties={"position":Position(posMachine["i"],posMachine["j"]),"number":4,"name":"green yoshi","score":0})
    posHuman =aBoard.getPosition(5,environment[0])
    playerHuman = Player(properties={"position":Position(posHuman["i"],posHuman["j"]),"number":5, "name":"red yoshi","score":0})
    WorldGenerator.updateMachinePos(machineMove[0], playerMachine, aBoard)
    environment.clear()
    environment.append(WorldGenerator.getOutput())
    aBoard = Board(environment[0])
    aBoard.setup()
    points = machinePoints[0]+ playerMachine.getScore()
    machinePoints.clear()
    machinePoints.append(points)
    print("Machine Human: ",humanPoints[0])
    print("Machine Machine: ",machinePoints[0])
    humanScore.set(str(humanPoints[0])+" :")
    machineScore.set(" : "+str(machinePoints[0]))
    endResult.set(Validation.validateGameResult(humanPoints[0], machinePoints[0], 24))
    showWorld(environment[0])
    aBoard.reset()
    BFS.reset()



#------------------------------------------- SEARCHTITLEFRAME WIDGETS---------------------------------
def showSearchSelected(searchName:str):
 pass



    
#--------------------------------------------------------------------------------------------------   
    

#------------------------------------------------------REPORTFRAME WIDGETS-------------------------
#Create and fix report 

#--------------------------------------------------------------------------------------------------   

#------------------------------------------GUI CREATION------------------------------------------
#Invocate function

def main():

#--------------------------------------------UPLOAD DATA FROM FILE----------------------------------------------------
    
    #
    #FileManager.uploadFile("Prueba1.txt")
  
    #environment.append(FileManager.getOutput())

    #WorldGenerator.execute()
    #environment.clear()
    #environment.append(WorldGenerator.getOutput())
    

    showGameTitle("Yoshi’s battle")
    showMenuOptions()
    #showUploadFileImage(fileImage)
    #chooseFile(os.getcwd())
    #showMenuOptions(searchImage,searchNames)
    #showWorld(environment[0])
    showEmptyWorld()
    #showReportEmpty()
    #showButton()
    

    #Generate constant loop
    root.mainloop()

main()

#------------------------------------------------------------------------------------------------

#---------------------------------------GUI EXECUTION------------------------------------------

#---------------------------------------------------------------------------------------------