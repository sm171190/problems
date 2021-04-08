import numpy as np

def choosePivot(N):
    return np.random.choice(N)

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
    
    A[0] = A[firstElementLargerThanPivotInPartition-1] 
    A[firstElementLargerThanPivotInPartition-1]  = pivot
    pivotIndexFinal = firstElementLargerThanPivotInPartition-1
    
    return (A,pivotIndexFinal)
    
def randSelect(A,i):    
    N = len(A)
    pivotId = choosePivot(N)    
    (partitioned,finalPivotIndex) = partition(A,pivotId)    
    if finalPivotIndex==(i-1):        
        return partitioned[finalPivotIndex]
    elif finalPivotIndex < (i-1):        
        return randSelect(A[finalPivotIndex:],(i-finalPivotIndex))
    else:        
        return randSelect(A[:finalPivotIndex],i)


N = 1000
arr = list(np.random.permutation(N))
i = 512

ith_smallest_element = randSelect(arr,i)

print(f'Array: \n{arr}')
print(f'{i}th smallest element: {ith_smallest_element}')