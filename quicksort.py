import numpy as np

def partition(A,pivotId):
    pivot = A[pivotId]
    temp = A[pivotId]    
    A[pivotId] = A[0]
    A[0]=temp

    N = len(A)
    nextIdToSee = 1
    firstElementLargerThanPivotInPartition = 1

    while nextIdToSee<N:
        seenNum = A[nextIdToSee]        

        if seenNum > pivot:
            pass
        else:
            temp  = A[firstElementLargerThanPivotInPartition]
            A[firstElementLargerThanPivotInPartition] = seenNum
            A[nextIdToSee] = temp
            firstElementLargerThanPivotInPartition+=1
        
        nextIdToSee+=1
        # print(A)
    
    A[0] = A[firstElementLargerThanPivotInPartition-1] 
    A[firstElementLargerThanPivotInPartition-1]  = pivot
    pivotIndexFinal = firstElementLargerThanPivotInPartition-1
    
    return (A,pivotIndexFinal)

def choosePivot(size):   
    # print(f'size: {size}') 
    return np.random.choice(size)    

def quickSort(A):
    # print(f'A: {A}')
    N = len(A)
    if N==1:
        return A
    
    else:
        pivotId = choosePivot(N)     
        # print(f'PivotId: {pivotId}')       
        (B,pivotIdNew) = partition(A,pivotId)
        L = B[:pivotIdNew]
        R = B[pivotIdNew+1:]
        leftSorted=list()
        rightSorted=list()
        if(len(L)>0):
            leftSorted = quickSort(L)
        if len(R)>0:
            rightSorted = quickSort(R)
        sorted = leftSorted
        sorted.append(A[pivotIdNew])
        for r in rightSorted:
            sorted.append(r)
        
        return sorted


        

N=1024
arr = list(np.random.permutation(N))
print(f'Original: {arr}')
print(f'Sorted: {quickSort(arr)}')
