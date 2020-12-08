def getCountOfPossibleTeams(coders):
    N = len(coders)
    R = coders
    count = 0
    firstPos = 0
    while(firstPos<N-2):
        secondPos = firstPos+1
        while(secondPos<N-1):
            thirdPos = secondPos+1
            while(thirdPos<N):
                if R[firstPos]<R[secondPos] and R[secondPos]<R[thirdPos] :
                    count=count+1
                elif R[firstPos]>R[secondPos] and R[secondPos]>R[thirdPos] :
                    count = count+1
                
                # print((firstPos,secondPos,thirdPos))
                thirdPos=thirdPos+1
            
            secondPos=secondPos+1
        firstPos=firstPos+1
    return count


print(getCountOfPossibleTeams([5,2,3,1,4]))
print(getCountOfPossibleTeams([2,5,3,1,4]))