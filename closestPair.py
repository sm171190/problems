import numpy as np
from math import sqrt

def mergeSort(arr,axis):
    N = len(arr)
    if N==2:
        if arr[0][axis]<arr[1][axis]:
            return arr
        else:
            return [arr[1],arr[0]]
    elif N==1:
        return arr
    else:
        N = int(N)
        L = mergeSort(arr[:N//2],axis)
        R = mergeSort(arr[N//2:],axis)
        S = list()
        pos_L = 0
        pos_R = 0
        pos_S = 0
        while(pos_S<N):
            if(pos_L < N//2 and pos_R < (N-N//2)):
                if L[pos_L][axis]  < R[pos_R][axis]:
                    S.append(L[pos_L])
                    pos_L+=1
                    pos_S+=1
                else:
                    S.append(R[pos_R])
                    pos_R+=1
                    pos_S+=1
        
            elif pos_L>= N//2 :
                S.append(R[pos_R])
                pos_R+=1
                pos_S+=1
            else:
                S.append(L[pos_L])
                pos_L+=1
                pos_S+=1
    
        return S


def findClosestPair(Px,Py):
    N = len(Px)    
    # print(f'N:{N}')
    if N<=4:
        minD = 1e4
        closestPair = None      
        for i in range(N-1):
            (x1,y1) = Px[i]
            for j in range(i+1,N):
                (x2,y2) = Px[j]
                d = sqrt((x1-x2)**2 + (y1-y2)**2)
                if d<minD:
                    minD = d
                    closestPair = [Px[i],Px[j]]
        # print(f'minD={minD}')
        # print(f'closestPair = {closestPair}')
        return (closestPair,minD)
    
    else:        
        Lx = Px[:N//2]
        Rx = Px[N//2:]
        Ly = list()
        Ry = list()
        (xMinLeft,xMaxLeft) = (Lx[0][0],Lx[N//2-1][0])
        for i in range(N):
            x = Py[i][0]
            if xMinLeft<= x <=xMaxLeft:
                Ly.append(Py[i])
            else:
                Ry.append(Py[i])        
        
        # print('Left')
        (closestPairLeft,deltaLeft) = findClosestPair(Lx,Ly)
        # print(f'deltaLeft={deltaLeft}')
        # print(f'closestPairLeft = {closestPairLeft}')
        
        # print('Right')
        (closestPairRight,deltaRight) = findClosestPair(Rx,Ry)
        # print(f'deltaRight={deltaRight}')
        # print(f'closestPairRight = {closestPairRight}')
        
        # print('Split')
        delta = min(deltaLeft,deltaRight)
        # print(f'Delta:{delta}')
        (closestPairSplit,deltaSplit) = findClosestSplitPair(Px,Py,delta)       
        # print(f'deltaSplit={deltaSplit}')
        # print(f'closestPairSplit = {closestPairSplit}')

        if deltaSplit<delta:
            # print('Here1')
            return (closestPairSplit,deltaSplit)
        else:
            if deltaLeft<deltaRight:
                # print('Here2')
                return (closestPairLeft,deltaLeft)
            else:
                # print('Here3')
                return (closestPairRight,deltaRight)

        

def findClosestSplitPair(Px,Py,delta):
    N = len(Px)
    (minX,maxX) = (Px[N//2][0]-delta,Px[N//2][0]+delta)
    F=list()
    for p in Py:
        if minX<=p[0]<=maxX:
            F.append(p)
    
    # print(f'F: {F}')
    Nf = len(F)
    # print(f'len(F): {Nf}')

    if(Nf==1):
        return([],delta)
        
        
    minD = delta
    closestPair = list()
    for i in range(Nf-1):
        (x1,y1) = F[i]
        stopAt = min(i+7,Nf)
        for j in range(i+1,stopAt):            
            (x2,y2) = F[j]
            d = sqrt((x1-x2)**2 + (y1-y2)**2)
            if d<minD:
                minD = d
                closestPair = [F[i],F[j]]
    
    return (closestPair,minD)
                    
                
                


N=1023
P_array = np.random.randn(N,2,1)

P=list()
for i in range(N):
    P.append((P_array[i][0][0],P_array[i][1][0]))

point = (42,42)
P.append(point)
P.append(point)
print(f' Points: {P}')

Px = mergeSort(P,0)
Py = mergeSort(P,1)

(closestPair,closestD) = findClosestPair(Px,Py)
print(f'Closest Pair: {closestPair}')
print(f'Closest distance: {closestD}')