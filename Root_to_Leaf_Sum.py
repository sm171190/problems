def myDFS(AList,stack,done):    
    visited = []
    while(len(stack)>0):        
        currentNode = stack.pop()
        if(currentNode not in done):
            visited.append(currentNode)
            done.append(currentNode)   
        temp = []     
        for node in AList[currentNode]:
            if (node not in done):
                temp.append(node)            
        if(len(temp)==0):                                    
            return visited
        else:
            for node in temp:
                stack.append(node)

        
        
def cleanUp(AList,node):
    for nbrs in AList:
        for nbr in nbrs:
            if nbr==node:
                nbrs.remove(node)
    return AList



def checkSum(nodeList, leafNodes):
    if nodeList[len(nodeList)-1] in leafNodes:
        sum=0
        for node in nodeList:
            sum+=node                
    else:
        sum = None
    
    return sum

def getLeaves(AList):
    leaves = []
    for i in range(len(AList)):
        if len(AList[i])==1:
            leaves.append(i)
    return leaves
            


AdjList = [[1,2],[0,3,4],[0,5,6,7],[1],[1],[2,8],[2,9],[2,10],[5],[6],[7]]
initial_stack = []
root = 0 
initial_stack.append(root)
initial_done=[]
leaves = getLeaves(AdjList)
newAdjList = AdjList



for i in range(len(AdjList)):
    # print(newAdjList)
    initial_stack = []
    root = 0 
    initial_stack.append(root)
    initial_done=[]
    visitedNodes = myDFS(newAdjList,initial_stack,initial_done)
    print(visitedNodes)
    print(checkSum(visitedNodes,leaves))
    removeNode = visitedNodes[len(visitedNodes)-1]    
    newAdjList = cleanUp(newAdjList,removeNode)
