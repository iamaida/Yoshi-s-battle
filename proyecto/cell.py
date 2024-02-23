#-----------------------------------------------------------------------------------------------
# Course: Inteligencia Artificial
# Proffesor: Oscar Bedoya
# Topic: Proyecto 2
# Name:Aida Milena Mina Caicedo
# Code: 1225328
# Creation date: 17-11-2023
# Last modification date: 26-09-2023
#--------------------------------------------------------------------------------------------------------

class Cell:
    
    #Constructor
    def __init__(self, properties:dict):
        # Instance attribute
        self.properties=properties   

    def getPosition(self):
        return self.properties["position"]
    
    def getNumber(self):
        return self.properties["number"]
    
    def getColor(self):
        return self.properties["color"]
    
    def getName(self):
        return self.properties["name"]
    
    def isPlayerHere(self):
        return self.properties["playerHere"]
    
    def isAvailable(self):
        return self.properties["available"]
    
    #Habilitar
    def enable(self):
        self.properties["available"] = True
    
    #Deshabilitar
    def disable(self):
        self.properties["available"] = False
        
    #New Code
    def isAgentHere(self):
        return self.properties["agentHere"]
    
    def changeAgentHere(self):
        self.properties["agentHere"] = not(self.properties["agentHere"])

    def changePlayerToHere(self):
        self.properties["agentHere"] = True
    
    def removePlayerFromHere(self):
        self.properties["agentHere"] = False