
    
class Count:

    def availableCoins(board) -> int:
        counter:int =0
        for i,row in enumerate(board.get()):
          
            for j,cell in enumerate(row):
                if cell.getNumber()== 1 or cell.getNumber()== 3:
                    if cell.isAvailable():
                        counter = counter + 1
        return counter

    def getStateValues(node) -> dict:
        
        #agentBucket= node.getState().getAgent().getBucket()
        #agentBucketCap= agentBucket.getCapacity()
        #agentBucketLoad= agentBucket.getLoad()
        avaCoins =Count.availableCoins(node.getState().getBoard())
        #print({"capacity":agentBucketCap, "load":agentBucketLoad, "fires":actfires})
        return {"coins":avaCoins}

    
       