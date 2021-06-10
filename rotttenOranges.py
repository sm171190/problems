def newStateofCell(M,i,j):    
    R=len(M)
    C=len(M[0])
    if i==0:
        if j==0:
            if(M[i+1][j]==2 or M[i][j+1]==2):
                return 2
            else:
                return 1
        elif j==C-1:
            if(M[i+1][j]==2 or M[i][j-1]==2):
                return 2
            else:
                return 1
        else:
            if(M[i+1][j]==2 or M[i][j-1]==2 or M[i][j+1]==2):
                return 2
            else:
                return 1

    elif i==R-1:
        if j==0:
            if(M[i-1][j]==2 or M[i][j+1]==2):
                return 2
            else:
                return 1
        elif j==C-1:
            if(M[i-1][j]==2 or M[i][j-1]==2):
                return 2
            else:
                return 1
        else:
            if(M[i-1][j]==2 or M[i][j-1]==2 or M[i][j+1]==2):
                return 2
            else:
                return 1
    elif j==0:
        if i==0:
            if(M[i+1][j]==2 or M[i][j+1]==2):
                return 2
            else:
                return 1
        elif i==R-1:
            if(M[i-1][j]==2 or M[i][j+1]==2):
                return 2
            else:
                return 1
        else:
            if(M[i+1][j]==2 or M[i-1][j]==2 or M[i][j+1]==2):
                return 2
            else:
                return 1
    elif j==C-1:
        if i==0:
            if(M[i+1][j]==2 or M[i][j-1]==2):
                return 2
            else:
                return 1
        elif i==R-1:
            if(M[i-1][j]==2 or M[i][j-1]==2):
                return 2
            else:
                return 1
        else:
            if(M[i+1][j]==2 or M[i-1][j]==2 or M[i][j-1]==2):
                return 2
            else:
                return 1
    else:
        if(M[i+1][j]==2 or M[i-1][j]==2 or M[i][j-1]==2 or M[i][j+1]==2):
                return 2
        else:
            return 1
       
    

def updateState(Mat):
    R=len(Mat)
    C=len(Mat[0])
    NewMat=[[None for i in range(C)] for j in range(R)]
    # print('Initial NewMat:')
    # print(NewMat)    
    for r in range(R):
        for c in range(C):
            # print(f'({r},{c})')
            currnentState=Mat[r][c]
            if currnentState==0 or currnentState==2:
                # print('This state will not change!')                
                # print(f'currentState: {currnentState}')
                NewMat[r][c]=currnentState
                # print(NewMat)
                # return
            else:
                # print('This state will change!')
                NewMat[r][c] = newStateofCell(Mat,r,c)
    
    return NewMat

def hasChanged(lastM,currentM):
    R=len(lastM)
    C=len(lastM[0])    
    for r in range(R):
        for c in range(C):
            if lastM[r][c]!=currentM[r][c]:
                return True
    return False

def checkAllOranges(M):
    R=len(M)
    C=len(M[0])    
    for r in range(R):
        for c in range(C):
            if M[r][c]==1:
                return False
    return True

def rottenOrangesMain(M):
    last_M = M
    t=0
    while(True):
        if t > 2:
            return 0
        print(f't = {t}')            
        current_M = updateState(last_M)
        t+=1
        print('Last_M')
        print(last_M)
        print('current_M')
        print(current_M)
        if(hasChanged(last_M,current_M)):
            last_M=current_M
        else:
            print('No More Changes!')
            if checkAllOranges(current_M):
                return (t-1)
            else:
                return -1


################### driver ##########################
print('Enter the size of the matrix as space-separted positive integers:')
dims_String = input().split()
(NRows,NCols) = tuple(map(int,dims_String))
M = []
for r in range (NRows):    
    print(f'Enter the configuration of row {r}')
    config_Str = input().split()
    config_int = list(map(int,config_Str))
    M.append(config_int)

print(rottenOrangesMain(M))
    




                
                

    
