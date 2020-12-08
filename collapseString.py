def collapseString(inputString):
    if len(inputString) ==0 :
        return ""
    else:   
        finalString = ""     
        currentIndex = 0
        while(currentIndex<len(inputString)):
            currentChar = inputString[currentIndex]
            count = 0
            while(currentIndex<len(inputString) and inputString[currentIndex]==currentChar ):
                count=count+1
                currentIndex= currentIndex+1
            finalString = finalString+str(count)+currentChar
        return finalString




print(collapseString("GGGGGrrrrrrrrrrrrrrt"))
print(collapseString(""))
print(collapseString(" "))
print(collapseString("S"))
print(collapseString("dtrreflgggpoyyo"))